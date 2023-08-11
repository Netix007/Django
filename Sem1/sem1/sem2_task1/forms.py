from django import forms
from sem2_task1.models import Author


class AuthorForms(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))


class ArticleForms(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)
