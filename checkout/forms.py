# 3rd party imports

# Django imports
from django import forms

# Local imports
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Create a form of the order model in the checkout template
    """

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_num',
                  'street_address_1', 'street_address_2',
                  'town_or_city', 'county', 'postcode',
                  'country')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and class to each field
        and remove labels
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_num': 'Phone Number',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postcode / Zip Code',
            'country': 'Country',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control py-1'
            self.fields[field].label = False
