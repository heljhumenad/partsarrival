import pytest

from django.test import (
    TestCase,
    RequestFactory,
    Client,
)
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages import get_messages

from parts.app.tests.factories import (
    PartNumberFactory,
    PartNumberClassFactory,
    UnitofMeasureFactory,
    PartsArrivalFactory,
    ServiceAdvisorFactory
)


class BaseTestCase(TestCase):

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
