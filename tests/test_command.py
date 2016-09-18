from unittest import TestCase


class CommandTest(TestCase):
    def _getOne(self, *args, **kwargs):
        from soloftpd.command import Command
        return Command(*args, **kwargs)

    def test_make_parser(self):
        cmd = self._getOne()
        parser = cmd.make_parser()
        with self.subTest("config parameter"):
            result = parser.parse_args(['--config', 'test.config'])
            self.assertEqual(result.config, 'test.config')
        with self.subTest("address parameter"):
            result = parser.parse_args(['--address', '10.0.0.1'])
            self.assertEqual(result.address, '10.0.0.1')
        with self.subTest("port parameter"):
            result = parser.parse_args(['--port', '8021'])
            self.assertEqual(result.port, '8021')
        with self.subTest("masquerade address parameter"):
            result = parser.parse_args(['--masquerade-address', '172.0.0.1'])
            self.assertEqual(result.masquerade_address, '172.0.0.1')
        with self.subTest("username parameter"):
            result = parser.parse_args(['--username', 'test.user'])
            self.assertEqual(result.username, 'test.user')
        with self.subTest("password parameter"):
            result = parser.parse_args(['--password', 'test.password'])
            self.assertEqual(result.password, 'test.password')
        with self.subTest("directory parameter"):
            result = parser.parse_args(['--directory', 'test/directory'])
            self.assertEqual(result.directory, 'test/directory')
        with self.subTest("passive ports parameter"):
            result = parser.parse_args(['--passive-ports', '2000-2004'])
            self.assertEqual(result.passive_ports, (2000, 2004))
