from unittest import TestCase


class ConfigTest(TestCase):
    def _getOne(self):
        from soloftpd.config import Config
        return Config()

    def test_setattr(self):
        config = self._getOne()
        config.username = 'ham'
        with self.assertRaises(AttributeError):
            config.invalid_attribute = 'ham'

    def test_update(self):
        config = self._getOne()
        config.update(dict(address='10.0.0.1', port=10021))
        self.assertEqual(config.address, '10.0.0.1')
        self.assertEqual(config.port, 10021)
