from parts.app.tests.base import TestCase
from parts.app.forms.arrival_form import PartsArrivalForm


class TestArrivalForm(TestCase):

    def setUp(self):
        super().setUp()
        self._arrival_form = PartsArrivalForm()
