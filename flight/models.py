from django.db import models

class Airline(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    country = models.ForeignKey("Country")
    iata_code = models.CharField(_("IATA Code"), max_length=3, blank=True, null=True)

    class Meta:
        verbose_name = _("Airline")
        verbose_name_plural = _("Airlines")
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Airport(models.Model):
    iata_code = models.CharField(_("IATA Code"), max_length=3, primary_key=True)
    name = models.CharField(_("Name"), max_length=100)
    city = models.CharField(_("City"), max_length=100)
    country = models.ForeignKey("Country")


class Country(models.Model):
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Flight(models.Model):
    code = models.CharField(_("Flight Code"), max_length=7)
    airline = models.ForeignKey("Airline")
    from_airport = models.ForeignKey("Airport")
    to_airport = models.ForeignKey("Airport")
    seats = models.IntegerField()
    capacity = models.IntegerField()
