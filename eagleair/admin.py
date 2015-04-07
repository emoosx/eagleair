from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class EagleAirAdmin(AdminSite):
    site_title = ugettext_lazy("EagleAir")
    site_header = ugettext_lazy("EagleAir")

admin_site = EagleAirAdmin()
