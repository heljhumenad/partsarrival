from parts.app.tests.base import BaseTestCase
from parts.app.accounts.models import CustomUser


class TestsAccounts(BaseTestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            username='heljhum',
            first_name='Heljhum',
            last_name='Enad',
            email='heljhumenad@gmail.com',
            is_staff=True
        )

    def setUp(self):
        super().setUp()
        self.user = CustomUser.objects.get(username='heljhum')

    def test_accounts_get_user_name(self):
        # user = CustomUser.objects.get(username='heljhum')
        self.assertEqual(self.user.get_user_account_name,
                         "{0} {1}".format(self.user.last_name, self.user.first_name))

    def test_accounts_get_user_email(self):
        self.assertEqual(self.user.get_user_email, self.user.email)

    def test_accounts_valid_email(self):
        self.assertIn('@', self.user.get_user_email)
