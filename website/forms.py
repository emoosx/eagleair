from flight.models import Airport
from django import forms


class FrontPageSearchForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    no_of_guests = forms.ChoiceField(required=True,
                                     choices=[(i, i) for i in range(1, 11)],
                                     widget=forms.Select(attrs={'class': 'browser-default'}))
    departure = forms.ModelChoiceField(label='From',
                                      queryset=Airport.objects.all(),
                                      empty_label=None,
                                      widget=forms.Select(attrs={
                                          'class': 'browser-default'}))
    arrival = forms.ModelChoiceField(label='To', queryset=Airport.objects.all(),
                                     empty_label=None,
                                     widget=forms.Select(attrs={
                                         'class': 'browser-default'}))
