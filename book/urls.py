from django.urls import path
from .views import BookListView, BookDetailView, EditReviewView, DeleteBookReviewView, ConfirmationDeleteView, \
    reviews_like_dislike

app_name = 'book'

urlpatterns = [
    path('all/', BookListView.as_view(), name='book_list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:book_id>/edit/<int:review_id>/', EditReviewView.as_view(), name='edit_review'),
    path('<int:book_id>/delete/<int:review_id>/', DeleteBookReviewView.as_view(), name='delete_review'),
    path('<int:book_id>/delete-confirmation/<int:review_id>/', ConfirmationDeleteView.as_view(), name='delete-confirmation-review'),
    path('comment/<int:review_id>/<str:action>/', reviews_like_dislike, name='comment_like_dislike'),  # To‘g‘rilandi
]
