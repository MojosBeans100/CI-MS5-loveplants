# 3rd party imports

# Django imports
from django import forms
from django.forms import (Textarea, RadioSelect,
                          TextInput, NumberInput, Select)

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
            'friendly_name': TextInput(attrs={
                'placeholder': 'eg. Chinese Money Plant',
            }),
            'latin_name': TextInput(attrs={
                'placeholder': 'eg. pilea peperomioides',
            }),
            'description': Textarea(attrs={
                'placeholder': ('eg. Pilea peperomiodes, also known as '
                                'the Chinese money plant, missionary plant,'
                                ' pancake plant,'
                                ' the pass-it-along plant and the UFO plant..')
            }),
            'description_source': TextInput(attrs={
                'placeholder': 'eg. Happy House Plants',
            }),
            'description_url': TextInput(attrs={
                'placeholder': 'eg. www.happyhouseplants.com',
            }),
            'image1_source_url': TextInput(attrs={
                'placeholder': 'eg. https://res.cloudinary.com/...',
            }),
            'image1_source': TextInput(attrs={
                'placeholder': 'eg. The Spruce',
            }),
            'care_instructions': Textarea(attrs={
                'placeholder': ('eg. Plant your Pilea peperomiodes in well  '
                                'drained compost and place in a warm,'
                                ' bright spot that is not too sunny. ')
            }),
            'care_instructions_source': TextInput(attrs={
                'placeholder': 'eg. Happy House Plants',
            }),
            'care_instructions_url': TextInput(attrs={
                'placeholder': 'eg. www.happyhouseplants.com',
            }),
            'price': TextInput(attrs={
                'placeholder': 'eg. 10.99',
            }),
            'stock_quantity': NumberInput(attrs={
                'placeholder': 'eg. 8',
            }),

        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            if field_name != 'live_on_site':
                field.widget.attrs['class'] = 'form-control mb-4'

            if (field_name == 'image1_source_url' or
                    field_name == 'image2_source_url' or
                    field_name == 'image3_source_url'):

                field.widget.attrs['onchange'] = 'uploadImage(this);'
