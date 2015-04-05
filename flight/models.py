from django.db import models
from international.models import countries


class Airline(models.Model):
    name = models.CharField("Name", max_length=50)
    country = models.CharField(verbose_name='Country', max_length=2, choices=countries, blank=True)
    iata_code = models.CharField("IATA Code", max_length=3,
                                 blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Airlines"
        ordering = ("name",)

    def __unicode__(self):
        return self.name


class Airport(models.Model):
    iata_code = models.CharField("IATA Code", max_length=3, primary_key=True)
    name = models.CharField("Name", max_length=50)
    city = models.CharField("City", max_length=50)
    country = models.CharField(verbose_name='Country', max_length=2,
                               choices=countries, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s (%s)" % (self.city, self.iata_code)

    def __str__(self):
        return "%s (%s)" % (self.city, self.iata_code)


class Aircraft(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMOY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'First Class'),
        (BUSINESS_CLASS, 'Business Class'),
        (ECONOMOY_CLASS, 'Economy Class')
    )
    model = models.CharField("Model", max_length=16)
    seat_count_F = models.IntegerField(max_length=3, default=6)
    seat_count_B = models.IntegerField(max_length=3, default=20)
    seat_count_E = models.IntegerField(max_length=3, default=60)
    seats_in_a_row_F = models.IntegerField(default=2)
    seats_in_a_row_B = models.IntegerField(default=4)
    seats_in_a_row_E = models.IntegerField(default=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_seat_count(self, class_of_service):
        if class_of_service == self.FIRST_CLASS:
            return self.seat_count_F
        elif class_of_service == self.BUSINESS_CLASS:
            return self.seat_count_B
        else:
            return self.seat_count_E

    def __unicode__(self):
        return '{} (F: {}, B: {}, E: {})'.format(self.model, self.seat_count_F,
                              self.seat_count_B, self.seat_count_E)


class Flight(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMOY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'First Class'),
        (BUSINESS_CLASS, 'Business Class'),
        (ECONOMOY_CLASS, 'Economy Class')
    )
    code = models.CharField("Flight Code", max_length=7)
    airline = models.ForeignKey("Airline")
    aircraft = models.ForeignKey("Aircraft", blank=True, null=True)
    departure_date = models.DateField('Depature Date', default='1990-01-01')
    departure_time = models.TimeField('Depature Time', default='08:00')
    from_airport = models.ForeignKey("Airport",
                                     related_name="from_airport")
    arrival_date = models.DateField('Arrival Date', default='1990-01-01')
    arrival_time = models.TimeField('Arrival Time', default='08:00')
    to_airport = models.ForeignKey("Airport",
                                   related_name="to_airport")
    price_F = models.FloatField('Price First Class', default='25000')
    price_B = models.FloatField('Price Business Class', default='4500')
    price_E = models.FloatField('Price Economy Class', default='400')

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} : {} {} {} -> {} {} {}'.format(self.code,
                                                  self.departure_date,
                                                  self.departure_time,
                                                  self.from_airport,
                                                  self.arrival_date,
                                                  self.arrival_time,
                                                  self.to_airport)
