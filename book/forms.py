from django import forms

from book.models import BookReview


class BookReviewForm(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5, min_value=1)
    class Meta:
        model = BookReview
        fields = ['stars_given', 'comment']