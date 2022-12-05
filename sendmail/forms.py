from django import forms
from .models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={"class": "email-input", 'placeholder': 'Enter your e-mail'})
        }