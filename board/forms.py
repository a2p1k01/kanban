from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'author', 'status', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control input-sm'})
        self.fields['author'].widget.attrs.update({'class': 'form-select input-sm'})
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
