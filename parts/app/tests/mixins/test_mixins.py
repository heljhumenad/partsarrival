from django.urls import reverse_lazy

from parts.app.mixins import useraccount_mixins
from parts.app.tests.base import TestCase


class TestUserAccountMixins(TestCase):

    def setUp(self):
        super().setUp()
        self._user_account_mixins = useraccount_mixins.UserAccountMixins

    def tests_class_has_account_mixins_attr(self):
        self.mixins = getattr(self._user_account_mixins, "login_url")
        self.assertTrue(self.mixins)

    def test_urls_for_accounts_mixins_redirect(self):
        self.mixins_url = getattr(self._user_account_mixins, "login_url")
        self.assertEqual(self.mixins_url, reverse_lazy(
            'login'))
