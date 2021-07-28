from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='City')


class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city name'}))

    class Meta:
        model = City
        fields = ('name',)