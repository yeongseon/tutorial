from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from contacts.models import (
    Contact,
    Address,
)

ContactAddressFormSet = inlineformset_factory(
    Contact,
    Address,
)

class ContactForm(forms.ModelForm):

    confirm_email = forms.EmailField(
        label = "Confirm email",
        required=True,
        )
    
    def clen(self):
        if (self.cleaned_data.get('email') !=
            self.cleaned_data.get('cofirm_email')):
            raise ValidationError(
                "Email addresses must match."
            )
        return self.cleaned_data

class Meta:
    model = Contact

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(ContactForm, self).__init__(*args, **kwargs)
