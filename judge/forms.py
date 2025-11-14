from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class SubmissionForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':80}), label='Your solution')
