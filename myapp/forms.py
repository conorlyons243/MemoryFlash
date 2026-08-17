from django.forms import ModelForm
from .models import Deck, Card
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django import forms

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["front", "back"] # Need to update if more fields are added (eg. images)

CardFormSet = inlineformset_factory(
    Deck,
    Card, 
    form=CardForm,
    extra=2, # Extra means num empty forms shown 
    max_num=1000,
    validate_max=True,
    min_num=2,
    validate_min=True,
    can_delete=True,
    can_order=True,
    # Change how the elements appear in the card forms
    widgets={
        "front": forms.Textarea(attrs={"rows": 5, "cols": 35}),
        "back": forms.Textarea(attrs={"rows": 5, "cols": 35})
    }
)

