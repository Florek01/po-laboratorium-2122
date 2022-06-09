from django import forms
from .models import Client, Address, Account


class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class FormAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class FormAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
