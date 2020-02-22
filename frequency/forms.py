from django import forms
from .models import givenurl
class urlform(forms.ModelForm):
	URL=forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		}

		))
	class Meta:
		model=givenurl
		fields=['URL']