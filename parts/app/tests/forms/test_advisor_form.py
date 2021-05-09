from parts.app.tests.base import TestCase
from parts.core.forms import AdvisorForm
from parts.app.tests.factories import ServiceAdvisorFactory

class TestAdvisorForm(TestCase):

    def setUp(self):
        super().setUp()
        self.advisor_factory = ServiceAdvisorFactory
        self.advisor_form = AdvisorForm()
    
    def test_advisor_form_instance(self):
        form = AdvisorForm()
        self.assertTrue(form, AdvisorForm())
    
    def test_blank_field(self):
        form = AdvisorForm()
        self.assertFalse(form.is_valid())
    
    def test_form_valid(self):
        form = AdvisorForm(data={self.advisor_factory})
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid)
    
    def test_clean_qty(self):
        form = AdvisorForm(data={'first_name': 'Pedro'})
        self.assertTrue(form.clean_first_name)
        self.assertTrue(form.fields['first_name'].required)
    
    def test_advisor_field(self):
        form = AdvisorForm({})
        self.assertTrue(form.fields['first_name'])
    
    def test_form_invalid(self):
        data = {}
        form = AdvisorForm(data)
        self.assertFalse(form.is_valid())
    
    def test_form_queryset_firstname(self):
        form = AdvisorForm({})
        self.assertTrue(form.fields['first_name'])

