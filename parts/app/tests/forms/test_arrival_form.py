from datetime import date, datetime

from parts.app.tests.base import TestCase
from parts.app.tests.factories import PartsArrivalFactory
from parts.core import validators
from parts.core.forms import PartsArrivalForm


class TestArrivalForm(TestCase):

    def setUp(self):
        super().setUp()
        self.arrival_factory = PartsArrivalFactory
        self.arrival_form = PartsArrivalForm()

    def test_form_instance(self):
        instance = hasattr(PartsArrivalForm, "PartsArrivalForm")
        self.assertFalse(instance)

   
    def test_blank_field(self):
        form = PartsArrivalForm({})
        self.assertFalse(form.is_valid())
   
    def test_form_valid(self):
        form = PartsArrivalForm(data={self.arrival_factory})
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid)
    
    def test_form_invalid(self):
        data = {
            'ro_number': 'RO012341',
            'customer_name': 'Juan Dela Cruz',
            'qty': 12,
            'item_class': 'WTY',
            'advisor': 'Pedro Sapanta',
            'remarks': 'Completed',
        }
        form = PartsArrivalForm(data)
        self.assertFalse(form.is_valid())

    def test_clean_qty(self):
        form = PartsArrivalForm(data={'qty': 12})
        self.assertTrue(form.clean_qty)
        self.assertTrue(form.fields['qty'].required)
        self.assertTrue(form.clean_ro_number)

    def test_arrival_field(self):
        form = PartsArrivalForm({})
        self.assertTrue(form.fields['ro_number'])
        self.assertTrue(form.fields['customer_name'])
        self.assertTrue(form.fields['qty'])
        self.assertTrue(form.fields['partnumber'])
        self.assertTrue(form.fields['advisor'])
        self.assertTrue(form.fields['item_class'])
        self.assertTrue(form.fields['date_arrival'])
    
    def test_arrival_instance_field(self):
        form = PartsArrivalForm(data={self.arrival_factory})    
         
