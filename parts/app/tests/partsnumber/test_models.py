from django.test import TestCase
import pytest

from parts.app.partsnumber.models import PartsNumber
from parts.app.tests.factories import PartNumberFactory


class TestModelPartsnumber(TestCase):

    def setUp(self):
        super().setUp()
        self.parts = PartNumberFactory()
        self.partnumber = self.parts.partnumber

    def test_str(self):
        self.asesertEqual(self.parts.__str__(), self.partnumber)

    def tearDown(self):
        pass
