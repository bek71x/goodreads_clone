from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import BookReview
from .serializers import BookDetailSerializer

class BookReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookDetailSerializer(book_review)
        return Response(serializer.data)

    def delete(self,request,id):
        book_review = BookReview.objects.get(id=id)
        book_review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BookReviewListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request, view=self)

        if page_obj is not None:
            serializer = BookDetailSerializer(page_obj, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = BookDetailSerializer(book_reviews, many=True)
        return Response(serializer.data)
