from django import forms
from .models import Playdate

class PlaydateForm(forms.ModelForm):
    class Meta:
        model = Playdate
        fields = ['date', 'friend']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }