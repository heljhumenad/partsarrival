from django import forms
from django.utils.translation import ugettext_lazy as _

from parts.app.forms import baseform
from parts.app.tests.base import TestCase


class TestBaseForm(TestCase):

    def setUp(self):
        super().setUp()
        self._base_form = baseform.BaseForms()

    def test_instance_for_base_form(self):
        self.assertEqual(self._base_form, isinstance(baseform.BaseForms())
