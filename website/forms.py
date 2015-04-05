from flight.models import Airport
from django import forms
from django.forms import Widget
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.forms import ValidationError
import datetime


DATE_FORMAT = '%d %B, %Y' # 17 April, 2015
class DatePickerWidget(Widget):
    def __init__(self, attrs=None):
        super(DatePickerWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        output = format_html(u'<input type="date" {0}>', flatatt(final_attrs))
        return output

    def value_from_datadict(self, data, files, name):
        date_data = data.get(name, '')
        try:
            D = datetime.datetime.strptime(date_data, DATE_FORMAT).date()
            return D
        except ValueError:
            return ''


class FrontPageSearchForm(forms.Form):
    TRIP_TYPES = (
        ('one', 'One Way'),
        ('round', 'Round Trip')
    )
    error_css_class = 'error'
    required_css_class = 'required'

    trip_type = forms.ChoiceField(required=True,
                                  choices=TRIP_TYPES,
                                  widget=forms.RadioSelect(attrs={
                                      'class': 'with-gap'}))
    no_of_guests = forms.IntegerField(required=True)
    departure = forms.ModelChoiceField(label='From',
                                      queryset=Airport.objects.all(),
                                       required=True,
                                      empty_label=None,
                                      widget=forms.Select)
    arrival = forms.ModelChoiceField(label='To', queryset=Airport.objects.all(),
                                     required=True,
                                     widget=forms.Select)
    depature_date = forms.DateField(widget=DatePickerWidget(attrs={
        'class': 'datepicker'}), required=True, initial=datetime.date.today)
    arrival_date = forms.DateField(widget=DatePickerWidget(attrs={
        'class': 'datepicker'}), required=False)


    def clean(self):
        cleaned_data = super(FrontPageSearchForm, self).clean()
        departure = cleaned_data.get('departure')
        arrival = cleaned_data.get('arrival')
        departure_date = cleaned_data.get('depature_date')
        arrival_date = cleaned_data.get('arrival_date')


        if departure and arrival:
            if departure == arrival:
                raise ValidationError(('Invalid travel destinations'),
                                      code='invalid')

        if departure_date:
            if departure_date < datetime.date.today():
                raise ValidationError(("Choose a sensible date!"),
                                      code='invalid')

        if departure_date and arrival_date:
            if arrival_date < departure_date:
                raise forms.ValidationError(("Error! Arrival date can't be before Depature Date!"), code='invalid')
