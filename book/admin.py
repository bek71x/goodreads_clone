from django.contrib import admin
from .models import Book,Author,BookAuthor,BookReview


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'cover']
    list_filter = ['title', 'isbn']
    search_fields = ['title','description']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'bio']

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['stars_given', 'book','user']
    list_filter = ['user','stars_given']
    search_fields = ['users','book']

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['book', 'author']
    list_filter = ['author']




admin.site.register(Book,BookAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Author, AuthorAdmin)

