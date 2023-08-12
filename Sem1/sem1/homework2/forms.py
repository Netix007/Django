from django import forms


class ItemForms(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()


class ImageForm(forms.Form):
    image = forms.ImageField()