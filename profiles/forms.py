# 3rd party imports

# Django imports
from django import forms

# Local imports
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and class to each field
        and remove labels
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_num': 'Phone Number',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postcode / Zip Code',
            'default_country': 'Country',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control py-1 my-3'
            self.fields[field].label = False
