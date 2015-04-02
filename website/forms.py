from django import forms


class FrontPageSearchForm(forms.Form):
    no_of_guests = forms.ChoiceField(required=True)
    # departure = forms.ChoiceField(label=_('From'), required=True, choices=)
    # arrival = forms.ChoiceField(label=_('To'), required=True, choices=)
