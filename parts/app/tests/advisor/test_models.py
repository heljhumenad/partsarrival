from parts.app.tests.base import TestCase


class TestsAdvisor(TestCase):

    def setUp(self):
        super().setUp()

    def test_str_dunder(self):
        first_name, last_name = self.advisor.first_name, self.advisor.last_name
        self.assertEqual(self.advisor.__str__(),
                         "{0} {1}".format(first_name, last_name))
