import argparse
import logging

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .config import Config
from .authorizers import Authorizer

logger = logging.getLogger(__name__)


class Command:
    handler_class = FTPHandler
    server_class = FTPServer
    authorizer_class = Authorizer

    def make_parser(self):
        parser = argparse.ArgumentParser(description="Run soloftpd server.")
        parser.add_argument('--config', help="Use config file")
        return parser

    def make_authorizer(self, config):
        return self.authorizer_class(
            config.username,
            config.password,
            config.directory,
            config.permission)

    def make_handler(self, config, authorizer):
        handler = self.handler_class
        handler.authorizer = authorizer
        handler.masquerade_address = config.masquerade_address
        handler.passive_ports = range(*config.passive_ports)
        return handler

    def make_server(self, config, handler):
        server = self.server_class((config.address, config.port), handler)
        return server

    def __call__(self):
        parser = self.make_parser()
        args = parser.parse_args()
        config_file = args.config
        if config_file:
            logger.info("Using config file: %s", config_file)
            config = Config.from_file(config_file)
        else:
            config = Config()
        authorizer = self.make_authorizer(config)
        handler = self.make_handler(config, authorizer)
        server = self.make_server(config, handler)
        server.serve_forever()


def main():
    Command()()


if __name__ == '__main__':
    main()
