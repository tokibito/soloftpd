from unittest import TestCase
from unittest import mock


class ApplicationTest(TestCase):
    def _getOne(self, *args, **kwargs):
        from soloftpd.app import Application
        return Application(*args, **kwargs)

    def test_make_command(self):
        from soloftpd.command import Command
        application = self._getOne()
        cmd = application.make_command()
        self.assertIsInstance(
            cmd, Command,
            "It makes Command instance.")

    def test_make_server(self):
        from soloftpd.server import Server
        application = self._getOne()
        server = application.make_server(None)
        self.assertIsInstance(
            server, Server,
            "It makes Server instance.")

    def test_run(self):
        application = self._getOne()
        with mock.patch('soloftpd.app.Server.start') as m:
            application.run([])
            m.assert_called_once_with()


class MainTest(TestCase):
    def _callFUT(self, *args, **kwargs):
        from soloftpd.app import main
        return main(*args, **kwargs)

    def test_it(self):
        class TestApp:
            def __init__(self):
                self.called = False

            def run(self):
                self.called = True

        self.assertTrue(self._callFUT(TestApp).called)
