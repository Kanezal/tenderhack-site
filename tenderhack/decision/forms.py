from django import forms
from .models import MainContract

class MainContractForm(forms.ModelForm):
    class Meta:
        model = MainContract
        exclude = ['customer_details', 'performer_details', 'is_being_edited', 'last_edited_by']