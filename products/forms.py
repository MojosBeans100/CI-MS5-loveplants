# 3rd party imports

# Django imports
from django import forms
from django.forms import Textarea, RadioSelect

# Local imports
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('review', 'rating', 'product')

        widgets = {
            'product': forms.HiddenInput(),
            'review': Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Leave your review for this product',
            }),
            'rating': RadioSelect(choices='rating', attrs={
                'onchange': 'colorRating();'
            }),
        }