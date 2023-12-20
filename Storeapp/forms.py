from django import forms
from .models import CardData
from .models import ContactMessage

class CardDataForm(forms.ModelForm):
    class Meta:
        model = CardData
        fields = ['card_number', 'card_owner', 'cvv_code', 'year_expiration', 'month_expiration']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
