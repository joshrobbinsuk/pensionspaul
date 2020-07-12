from django import forms
from django.forms import ModelForm
from .models import Fund


class AnalysisForm(forms.Form):
    pot_size = forms.IntegerField(max_value=1000000, min_value=1)
    years = forms.IntegerField(max_value=99, min_value=1)
    drawdown = forms.IntegerField(max_value=99, min_value=0)



class FundForm2(forms.Form):
    brand = forms.ModelChoiceField(queryset=Fund.objects.all())
    pot_size = forms.IntegerField(max_value=1000000, min_value=1)
    drawdown = forms.IntegerField(max_value=99, min_value=0)



# not used at present
class FundForm(ModelForm):  
    class Meta:
        model = Fund
        fields = ["brand"]