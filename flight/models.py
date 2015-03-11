from django.db import models


class Airline(models.Model):
    name = models.CharField("Name", max_length=100)
    country = models.ForeignKey("Country")
    iata_code = models.CharField("IATA Code", max_length=3,
                                 blank=True, null=True)

    class Meta:
        verbose_name_plural = "Airlines"
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Airport(models.Model):
    iata_code = models.CharField("IATA Code", max_length=3, primary_key=True)
    name = models.CharField("Name", max_length=100)
    city = models.CharField("City", max_length=100)
    country = models.ForeignKey("Country")


class Country(models.Model):
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Flight(models.Model):
    code = models.CharField("Flight Code", max_length=7)
    airline = models.ForeignKey("Airline")
    from_airport = models.ForeignKey("Airport", related_name="from_airport")
    to_airport = models.ForeignKey("Airport", related_name="to_airport")
    seats = models.IntegerField()
    capacity = models.IntegerField()
