from django import forms
from core.models import Waiting

class WaitingForm(forms.ModelForm):
    class Meta:
        model = Waiting
        fields = '__all__'