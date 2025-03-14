from django.shortcuts import render
from django.views import View
from book.models import Book

class BookListView(View):

    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'books/book_list.html', context)


class BookDetailView(View):


    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        context = {'book': book}
        return render(request, 'books/book_detail.html', context)
