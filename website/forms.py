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
    error_css_class = 'error'
    required_css_class = 'required'
    no_of_guests = forms.ChoiceField(required=True,
                                     choices=[(i, i) for i in range(1, 11)],
                                     widget=forms.Select(attrs={'class': 'browser-default'}))
    departure = forms.ModelChoiceField(label='From',
                                      queryset=Airport.objects.all(),
                                       required=True,
                                      empty_label=None,
                                      widget=forms.Select(attrs={
                                          'class': 'browser-default'}))
    arrival = forms.ModelChoiceField(label='To', queryset=Airport.objects.all(),
                                     required=True,
                                     empty_label=None,
                                     widget=forms.Select(attrs={
                                         'class': 'browser-default'}))
    depature_date = forms.DateField(widget=DatePickerWidget(attrs={
        'class': 'datepicker'}), required=True)
    arrival_date = forms.DateField(widget=DatePickerWidget(attrs={
        'class': 'datepicker'}), required=False)
