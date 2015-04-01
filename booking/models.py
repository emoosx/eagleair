from international.models import countries
from django.db import models



class Booking(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    first_name = models.CharField(verbose_name='First Name',
                                  max_length=20, blank=True)
    last_name = models.CharField(verbose_name='Sirname',
                                 max_length=20, blank=True)
    nationality = models.CharField(verbose_name='Nationality', max_length=2,
                                   choices=countries, blank=True)
    street1 = models.CharField(verbose_name='Street 1',
                               max_length=256, blank=True)
    street2 = models.CharField(verbose_name='Street 2',
                               max_length=256, blank=True)
    city = models.CharField(verbose_name='City',
                            max_length=256, blank=True)
    zipcode = models.CharField(verbose_name='Zip/Postal Code',
                               max_length=256, blank=True)
    country = models.CharField(verbose_name='Country', max_length=2,
                               choices=countries, blank=True)
    email = models.EmailField(verbose_name='Email')
    creation_date = models.DateTimeField(verbose_name='Creation Date',
                                         auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']

    def __unicode__(self):
        return '#{} ({})'.format(self.pk, self.creation_date)
