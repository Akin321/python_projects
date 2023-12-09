from django import forms
from . models import Food
class Foodf(forms.ModelForm):
    class Meta:
        model=Food
        fields=['name','desc','price','img']