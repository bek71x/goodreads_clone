from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from book.models import Book, BookReview
from .forms import BookReviewForm


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        search = request.GET.get('q')
        if search :
            books = books.filter(title__icontains=search)
        context = {'books': books}
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
