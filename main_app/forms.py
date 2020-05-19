from django import forms
from .models import Cat, Feeding

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ('name', 'breed', 'description', 'age')


class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
