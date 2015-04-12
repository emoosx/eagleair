from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy
from django import forms

ERROR_MESSAGE = "Error logging in!"

class UserAdminAuthenticationForm(AuthenticationForm):
    login_form = forms.BooleanField(widget=forms.HiddenInput,
                                    initial=1,
                                    error_messages={'required': ugettext_lazy(
                                    "Please log in again, because your session has expired.")})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ERROR_MESSAGE

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                if u'@' in username:
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your username." +
                                        " Try %s instead") % user.username
                raise forms.ValidationError(message)
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        return self.cleaned_data


class UserAdmin(AdminSite):
    site_title = ugettext_lazy("EagleAir")
    site_header = ugettext_lazy("EagleAir")
    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


user_admin_site = UserAdmin(name='useradmin')
