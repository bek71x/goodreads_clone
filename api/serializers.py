from rest_framework import serializers

from book.models import BookReview, Book
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','first_name','last_name','profile_picture','gender']


class BookDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = BookReview
        fields = ['id', 'stars_given','comment','book','user','created_at']