from django import forms
from .models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['label', 'description', 'main_form']
        
        widgets = {
            'main_form': forms.HiddenInput(),
        }