from django import forms
from parts.app.tests.base import TestCase
from parts.app.forms.partsnumber_form import PartsNumberForm
from parts.app.tests.factories import PartNumberFactory
from parts.core import validators

class TestPartnumberForm(TestCase):
    
    def setUp(self):
        super().setUp()
        self.partnumber_factory = PartNumberFactory
        self.partnumber_form = PartsNumberForm()

    def test_partnumber_instance(self):
        form = PartsNumberForm()
        self.assertTrue(self.partnumber_form, form)
    
    def test_blank_partnumber_field(self):
        form = PartsNumberForm({})
        self.assertFalse(form.is_valid())
    
    def test_partnumber_form_valid(self):
        form = PartsNumberForm(data={self.partnumber_factory})
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid)
    
    def test_partnumber_form_invalid(self):
        data =  {}
        form = PartsNumberForm(data)
        self.assertFalse(form.is_valid())
    
    def test_clean_partnumber(self):
        form = PartsNumberForm(data={'partnumber': 'DEO1L-10W30'})
        self.assertTrue(form.clean_partnumber)
        self.assertTrue(len(str(form.clean_partnumber)), validators.MAX_VALUE_OF_PARTNUMBER)
        self.assertEqual(form.fields['partnumber'].label, 'Parts Number')
        self.assertIn(form.errors.as_data(), {'partnumber': [forms.ValidationError(['Partnumbe size is not valid'])]})
                