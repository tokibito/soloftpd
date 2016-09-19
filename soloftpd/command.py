import os
import argparse
import logging
import logging.config

from .config import Config

logger = logging.getLogger(__name__)


def passive_ports(ports_text):
    if not ports_text:
        return
    start, end = ports_text.split('-', 1)
    return int(start), int(end)


class Command:
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

    def override_config(self, config, args):
        updates = {}
        for key, value in vars(args).items():
            if key == 'config':
                continue
            if value is not None:
                updates[key] = value
        config.update(updates)

    def parse(self, args=None):
        parser = self.make_parser()
        args = parser.parse_args(args)
        config_file = args.config
        if os.path.exists(config_file):
            logger.info("Using config file: %s", config_file)
            config = Config.from_file(config_file)
        else:
            logger.info(
                "File not exists: %s, using default config...", config_file)
            config = Config()
        self.override_config(config, args)
