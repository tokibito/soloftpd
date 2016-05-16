import argparse
import logging

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .config import Config
from .authorizers import Authorizer

logger = logging.getLogger(__name__)


class Command:
    def make_parser(self):
        parser = argparse.ArgumentParser(description="Run soloftpd server.")
        parser.add_argument('--config', help="Use config file")
        return parser

    def make_authorizer(self, config):
        return Authorizer(config.username, config.password, config.permission)

    def make_handler(self, config, authorizer):
        handler = FTPHandler()
        handler.authorizer = authorizer
        handler.masquerade_address = config.masquerade_address
        handler.passive_ports = range(*config.passive_ports)
        return handler

    def make_server(self, config, handler):
        server = FTPServer((config.address, config.port), handler)
        return server

    def __call__(self):
        parser = self.make_parser()
        args = parser.parse_args()
        config_file = args.config
        if config_file:
            logger.info("Using config file: %s", config_file)
            config = Config.from_file(self.config_file)
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
