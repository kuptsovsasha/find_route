from django import forms

from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))

    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))

    travelling_time = forms.IntegerField(label='time on road', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'time on road'}))
    cities = forms.ModelMultipleChoiceField(label='throw cities', queryset=City.objects.all(), required=False,
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'form-control js-example-basic-multiple'}))





    # class Meta:
    #     model =
    #     fields = '__all__'
