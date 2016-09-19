from unittest import TestCase
from unittest import mock


class ServerTest(TestCase):
    def _getOne(self, *args, **kwargs):
        from soloftpd.server import Server
        return Server(*args, **kwargs)

    def test_make_authorizer(self):
        from soloftpd.authorizers import Authorizer
        server = self._getOne()
        authorizer = server.make_authorizer(server.config)
        self.assertIsInstance(authorizer, Authorizer)

    def test_make_handler(self):
        from pyftpdlib.handlers import FTPHandler
        server = self._getOne()
        handler = server.make_handler(server.config, None)
        self.assertEqual(handler, FTPHandler)

    def test_make_server(self):
        from pyftpdlib.servers import FTPServer
        server = self._getOne()
        server.config.port = 30021
        ftp_server = server.make_server(server.config, None)
        self.assertIsInstance(ftp_server, FTPServer)

    def test_start(self):
        server = self._getOne()
        server.config.port = 40021
        with mock.patch('soloftpd.server.FTPServer.serve_forever') as m:
            server.start()
            m.assert_called_once_with()
