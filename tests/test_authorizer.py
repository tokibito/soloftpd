from unittest import TestCase


class MakePasswordHashTest(TestCase):
    def _callFUT(self, *args, **kwargs):
        from soloftpd.authorizers import make_password_hash
        return make_password_hash(*args, **kwargs)

    def test_valid_password(self):
        self.assertEqual(
            self._callFUT("spam"),
            "ded982e702e07bb7b6effafdc353db3fe172c83f"
        )
