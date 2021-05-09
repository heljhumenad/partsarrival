from parts.app.tests.base import TestCase
from parts.app.partsnumber.models import PartsNumber


class TestModelPartsnumber(TestCase):

    def setUp(self):
        super().setUp()

    def test_str(self):
        self.assertEqual(self.parts.__str__(), self.partnumber)
        self.assertEqual(self.item_class.__str__(),
                         self.item_class_number)
        self.assertEqual(self.um_class.__str__(), self.unit_of_measure)
    
    def test_add_leading_zero(self):
        selling_price = str(self.parts.selling_price) + ".00"
        self.assertEqual(selling_price, self.parts.add_leading_zero) 
