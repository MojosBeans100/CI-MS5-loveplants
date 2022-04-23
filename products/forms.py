# 3rd party imports

# Django imports
from django import forms
from django.forms import Textarea, RadioSelect

# Local imports
from .models import ProductReview, Product


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


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'sunlight': RadioSelect(choices='sun_or_water'),
            'watering': RadioSelect(choices='sun_or_water'),
            'care_required': RadioSelect(choices='care_demand'),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():

            if field_name != 'sunlight':
                field.widget.attrs['class'] = 'form-control mb-4'

    