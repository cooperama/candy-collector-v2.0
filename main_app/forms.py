from django import forms
from .models import Candy, Store

class CandyForm(forms.ModelForm):
    class Meta:
        model = Candy
        fields = [
            'name', 
            'description', 
            'ingredients', 
            'price'
        ]

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'store_name',
            'location',
            'description'
        ]