import os
import argparse
import logging
import logging.config

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .config import Config
from .authorizers import Authorizer

logger = logging.getLogger(__name__)


def passive_ports(ports_text):
    if not ports_text:
        return
    start, end = ports_text.split('-', 1)
    return int(start), int(end)


class Command:
    handler_class = FTPHandler
    server_class = FTPServer
    authorizer_class = Authorizer

    def make_parser(self):
        parser = argparse.ArgumentParser(description="Run soloftpd server.")
        parser.add_argument(
            '--config', help="Use config file", default="/etc/soloftpd.conf")
        parser.add_argument(
            '--address', help="Bind address")
        parser.add_argument(
            '--port', help="Bind port")
        parser.add_argument(
            '--masquerade-address', help="Masquerade address")
        parser.add_argument(
            '--username', help="Username")
        parser.add_argument(
            '--password', help="Password")
        parser.add_argument(
            '--directory', help="Directory")
        parser.add_argument(
            '--passive-ports', help="Passive ports", type=passive_ports)
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
        # ex. [100, 200] => range(100, 201)
        handler.passive_ports = range(
            config.passive_ports[0], config.passive_ports[1] + 1)
        return handler

    def make_server(self, config, handler):
        server = self.server_class((config.address, config.port), handler)
        return server

    def override_config(self, config, args):
        updates = {}
        for key, value in vars(args).items():
            if key == 'config':
                continue
            if value is not None:
                updates[key] = value
        config.update(updates)

    def setup_logging(self, config):
        logging_config = {'version': 1, 'disable_existing_loggers': False}
        logging_config.update(config.logging)
        logging.config.dictConfig(logging_config)

    def __call__(self):
        parser = self.make_parser()
        args = parser.parse_args()
        config_file = args.config
        if os.path.exists(config_file):
            logger.info("Using config file: %s", config_file)
            config = Config.from_file(config_file)
        else:
            logger.info(
                "File not exists: %s, using default config...", config_file)
            config = Config()
        self.override_config(config, args)
        self.setup_logging(config)
        authorizer = self.make_authorizer(config)
        handler = self.make_handler(config, authorizer)
        server = self.make_server(config, handler)
        server.serve_forever()


def main():
    Command()()


if __name__ == '__main__':
    main()
