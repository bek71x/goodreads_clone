from django.urls import path

from api.views import BookReviewAPIView, BookReviewListAPIView
urlpatterns=[
    path('reviews/', BookReviewListAPIView.as_view(), name='reviews-list'),
    path('reviews/<int:id>/',BookReviewAPIView.as_view(),name='reviews-detail'),
]

