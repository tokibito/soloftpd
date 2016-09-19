from unittest import TestCase
import tempfile


class MakePasswordHashTest(TestCase):
    def _callFUT(self, *args, **kwargs):
        from soloftpd.authorizers import make_password_hash
        return make_password_hash(*args, **kwargs)

    def test_valid_password(self):
        self.assertEqual(
            self._callFUT("egg"),
            "4fa6024f12494d3a99d8bda9b7a55f7d140f328a"
        )


class AuthorizerTest(TestCase):
    def _getOne(self, *args, **kwargs):
        from soloftpd.authorizers import Authorizer
        return Authorizer(*args, **kwargs)

    def setUp(self):
        self.temp_directory_context = tempfile.TemporaryDirectory()
        self.temp_directory = self.temp_directory_context.__enter__()

    def tearDown(self):
        self.temp_directory_context.__exit__(None, None, None)

    def test_it(self):
        authorizer = self._getOne(
            username="spam",
            password="4fa6024f12494d3a99d8bda9b7a55f7d140f328a",
            directory=self.temp_directory)
        with self.subTest("has_user"):
            self.assertTrue(authorizer.has_user("spam"))
        with self.subTest("validate_password"):
            self.assertTrue(authorizer.validate_password("egg"))
        with self.subTest("validate_authentication"):
            self.assertIsNone(
                authorizer.validate_authentication("spam", "egg", None))
        with self.subTest("get_home_dir"):
            self.assertEqual(
                authorizer.get_home_dir("spam"),
                self.temp_directory)
        with self.subTest("has_perm"):
            self.assertTrue(authorizer.has_perm("spam", "e"))
        with self.subTest("get_perm"):
            self.assertEqual(authorizer.get_perms("spam"), "elradfmw")
        with self.subTest("get_msg_login"):
            self.assertEqual(
                authorizer.get_msg_login("spam"), "Login successful.")
        with self.subTest("get_msg_quit"):
            self.assertTrue(authorizer.get_msg_quit("spam"), "Goodbye.")
        with self.subTest("impersonate_user"):
            self.assertIsNone(authorizer.impersonate_user("spam", "egg"))
        with self.subTest("terminate_impersonation"):
            self.assertIsNone(authorizer.terminate_impersonation("spam"))
