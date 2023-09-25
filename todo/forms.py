from django import forms
from .models import Item


# Inherit all functionality of ModelForm
class ItemForm(forms.ModelForm):
    # provide inner class to tell form which model its going to be associated with
    class Meta:
        model = Item
        fields = ['name', 'done']