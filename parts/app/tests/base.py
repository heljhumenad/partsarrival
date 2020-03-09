import pytest

from django.test import TestCase
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

from parts.app.tests.factories import (
    PartNumberFactory,
    PartNumberClassFactory,
    UnitofMeasureFactory,
)


class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.parts = PartNumberFactory()
        self.item_class = PartNumberClassFactory()
        self.um_class = UnitofMeasureFactory()
        self.partnumber = self.parts.partnumber
        self.item_class_number = self.item_class.class_name
        self.unit_of_measure = self.um_class.um

    def tearDown(self):
        pass
