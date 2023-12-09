from django import forms
from .models import MainContract

class MainContractForm(forms.ModelForm):
    class Meta:
        model = MainContract
        fields = '__all__'