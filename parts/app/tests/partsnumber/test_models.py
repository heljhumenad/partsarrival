from parts.app.tests.base import BaseTestCase
from parts.app.partsnumber.models import PartsNumber


class TestModelPartsnumber(BaseTestCase):

    def setUp(self):
        super().setUp()

    def test_str(self):
        self.assertEqual(self.parts.__str__(), self.partnumber)
        self.assertEqual(self.item_class.__str__(),
                         self.item_class_number)
        self.assertEqual(self.um_class.__str__(), self.unit_of_measure)
