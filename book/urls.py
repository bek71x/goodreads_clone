from django.urls import path
from .views import BookListView, BookDetailView

app_name = 'book'  # book appiga murojaat uchun umumiy nom

urlpatterns = [
    path('all/', BookListView.as_view(), name='book_list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
]