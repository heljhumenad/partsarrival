import pytest
from django.contrib.messages import get_messages
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import Client, RequestFactory
from django.test import TestCase as BaseTestCase
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from parts.app.tests.factories import (PartNumberClassFactory,
                                       PartNumberFactory, PartsArrivalFactory,
                                       ServiceAdvisorFactory,
                                       UnitofMeasureFactory)


class TestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.parts = PartNumberFactory()
        self.item_class = PartNumberClassFactory()
        self.um_class = UnitofMeasureFactory()
        self.parts_arrival = PartsArrivalFactory()
        self.advisor = ServiceAdvisorFactory()
        self.partnumber = self.parts.partnumber
        self.item_class_number = self.item_class.class_name
        self.unit_of_measure = self.um_class.um

    def tearDown(self):
        pass
