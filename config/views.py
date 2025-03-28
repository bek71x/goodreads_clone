from django import views
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from book.models import BookReview, Book


def landing_page(request):

    return  render(request,template_name='landingpage.html')

def home(request):
    books = Book.objects.all()
    reviews = BookReview.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size',10)
    paginator = Paginator(reviews, page_size)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    context = {
        'books': books,
        'reviews': reviews,
        'page_obj': page_obj
    }

    return render(request, 'home.html', context)