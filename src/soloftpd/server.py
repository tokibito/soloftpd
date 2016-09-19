import logging
import logging.config

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .config import Config
from .authorizers import Authorizer

logger = logging.getLogger(__name__)


class Server:
    handler_class = FTPHandler
    server_class = FTPServer
    authorizer_class = Authorizer

    def __init__(self, config=None):
        self.config = config if config is not None else Config()
        self.server = None

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

    def setup_logging(self, config):
        logging_config = {'version': 1, 'disable_existing_loggers': False}
        logging_config.update(config.logging)
        logging.config.dictConfig(logging_config)

    def start(self):
        self.setup_logging(self.config)
        authorizer = self.make_authorizer(self.config)
        handler = self.make_handler(self.config, authorizer)
        self.server = self.make_server(self.config, handler)
        self.server.serve_forever()
