from django import forms
from deposits.models import Deposit


class AddDeposit(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]
