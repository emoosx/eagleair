from flight.models import Airport
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import Widget
from django.forms.utils import flatatt
from django.utils.html import format_html


class DatePickerWidget(Widget):
    def __init(self, attrs=None):
        super(DatePickerWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        output = format_html(u'<input type="date" {0}>', flatatt(final_attrs))
        return output



class FrontPageSearchForm(forms.Form):
    TRIP_TYPES = (
        ('one-way', 'One Way'),
        ('round', 'Round Trip')
    )
    error_css_class = 'error'
    required_css_class = 'required'

    trip_type = forms.ChoiceField(required=True,
                                  choices=TRIP_TYPES,
                                  widget=forms.RadioSelect(attrs={
                                      'class': 'with-gap'}))
    no_of_guests = forms.ChoiceField(required=True,
                                     choices=[(i, i) for i in range(1, 11)],
                                     widget=forms.Select)
    departure = forms.ModelChoiceField(label='From',
                                      queryset=Airport.objects.all(),
                                       required=True,
                                      empty_label=None,
                                      widget=forms.Select)
    arrival = forms.ModelChoiceField(label='To', queryset=Airport.objects.all(),
                                     required=True,
                                     empty_label=None,
                                     widget=forms.Select)
    depature_date = forms.DateField(widget=DatePickerWidget(attrs={
        'class': 'datepicker'}), required=True)
    arrival_date = forms.DateField(widget=DatePickerWidget(attrs={
        'class': 'datepicker'}), required=False)
