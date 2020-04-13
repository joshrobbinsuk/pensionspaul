from django import forms
from django.forms import ModelForm
from .models import Fund

class AnalysisForm(forms.Form):
	pot_size = forms.DecimalField(max_digits=9, decimal_places=2)
	years = forms.DecimalField(max_digits=9, decimal_places=2) 


class FundForm(ModelForm):
	class Meta:
		model = Fund
		fields = ['brand']

class FundForm2(forms.Form):
	brand = forms.CharField()
	pot_size = forms.DecimalField(max_digits=9, decimal_places=2)