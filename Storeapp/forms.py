from django import forms
from .models import CardData

class CardDataForm(forms.ModelForm):
    class Meta:
        model = CardData
        fields = ['card_number', 'card_owner', 'cvv_code', 'year_expiration', 'month_expiration']
