from website.forms import FrontPageSearchForm
import datetime
import unittest

DATE_FORMAT = '%d %B, %Y' # 17 April, 2015


class FormTests(unittest.TestCase):
    def test_validation(self):
        form_data = {
            'trip_type': 'one',
            'no_of_guests': 2,
            'departure': 'fDD',
            'arrival': 'g',
            'departure_date': '16 April, 2015',
            'arrival_date': '18 April, 2015'
        }
        form = FrontPageSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
