from django import forms
from .models import Bags, Scoops


class BagsForm(forms.ModelForm):

    class Meta:
        model = Bags
        fields = '__all__'


class ScoopsForm(forms.ModelForm):

    class Meta:
        model = Scoops
        fields = '__all__'
