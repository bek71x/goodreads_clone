from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from book.models import Book, BookReview, ReviewLikeDislike
from .forms import BookReviewForm


class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('-id')
        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 5)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {'books': books,
                   "page_obj": page_obj,}
        return render(request, 'books/book_list.html', context)


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        reviews = BookReview.objects.filter(book=book)[::-1]
        form = BookReviewForm()
        context = {
            'book': book,
            'reviews': reviews,
            'form': form,
        }
        return render(request, 'books/book_detail.html', context)

    @method_decorator(login_required)
    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        form = BookReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book:book_detail', book_id=book.id)

        reviews = BookReview.objects.filter(book=book)
        context = {'form': form, 'book': book, 'reviews': reviews}
        return render(request, 'books/book_detail.html', context)

class EditReviewView(View):
    def get(self, request, book_id, review_id):
        comment = get_object_or_404(BookReview, id=review_id)
        book = comment.book
        comments = BookReview.objects.filter(book=book).exclude(id=review_id)

        if comment.user != request.user:
            return redirect(reverse('book:book_detail', kwargs={'book_id': book_id}))

        comment_form = BookReviewForm(instance=comment)
        return render(request, 'books/edit_review.html', {'review_form': comment_form, 'book': book, 'comments': comments})

    def post(self, request, book_id, review_id):
        comment = get_object_or_404(BookReview, id=review_id)

        # Check if the user is authorized to edit the comment
        if comment.user != request.user:
            return redirect(reverse('book:book_detail', kwargs={'book_id': book_id}))

        comment_form = BookReviewForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(reverse('book:book_detail', kwargs={'book_id': book_id}))
        else:
            messages.error(request, "Please correct the error below.")

        return render(request, 'books/edit_review.html', {'review_form': comment_form})

class ConfirmationDeleteView(View):
    def get(self, request, book_id, review_id):
        comment = BookReview.objects.get(id=review_id)
        book = Book.objects.get(id=book_id)

        return render(request, 'books/del_con.html', {'book': book, 'review': comment})

class DeleteBookReviewView(View):
    def get(self, request, book_id, review_id):
        review = BookReview.objects.get(id=review_id)
        review.delete()
        return redirect(reverse('book:book_detail', kwargs={'book_id': book_id}))

@login_required(login_url='user:login')
def reviews_like_dislike(request, review_id, action):
    comment = get_object_or_404(BookReview, id=review_id)
    existing_vote = ReviewLikeDislike.objects.filter(user=request.user, comment=comment).first()

    if existing_vote:
        if (action == 'like' and existing_vote.is_like) or (action == 'dislike' and not existing_vote.is_like):
            existing_vote.delete()  # Agar user o‘z ovozini qayta bossa, o‘chiramiz
        else:
            existing_vote.is_like = (action == 'like')
            existing_vote.save()
    else:
        ReviewLikeDislike.objects.create(user=request.user, comment=comment, is_like=(action == 'like'))

    return redirect('book:book_detail', book_id=comment.book.id)