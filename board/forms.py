from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Issue, User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['email'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control input-sm'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['password'].widget.attrs.update({'class': 'form-control input-sm'})


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'status', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['type'].widget.attrs.update({'class': 'form-select input-sm'})
        self.fields['status'].widget.attrs.update({'class': 'form-select input-sm'})


class DetailIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['status', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].widget.attrs.update({'class': 'form-select input-sm'})
        self.fields['status'].widget.attrs.update({'class': 'form-select input-sm'})
