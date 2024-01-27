from .models import register

from django import forms

class registerform(forms.ModelForm):
    class meta:
        model=register
        fields=['Name','Email_address','Mobile_Number','address','city','state','zip']