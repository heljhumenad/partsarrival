from parts.app.accounts.models import CustomUser
from parts.app.tests.base import TestCase
from parts.core.util import max_length_field, null_value_field


class TestsAccounts(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            username='sadmin',
            first_name='Nissan System',
            last_name='Administrator',
            email='it@nissancebu.com.ph',
            is_staff=True
        )

    def setUp(self):
        super().setUp()
        self.user = CustomUser.objects.get(username='sadmin')

    def test_accounts_get_user_name(self):
        # user = CustomUser.objects.get(username='heljhum')
        self.assertEqual(self.user.get_user_account_name,
                         "{0} {1}".format(self.user.first_name, self.user.last_name))
    def test_accounts_get_user_email(self):
        self.assertEqual(self.user.get_user_email, self.user.email)

    def test_accounts_valid_email(self):
        self.assertIn('@', self.user.get_user_email)
