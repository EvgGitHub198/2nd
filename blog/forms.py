from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'website': forms.TextInput(attrs={'placeholder': 'Enter your website'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),


        }