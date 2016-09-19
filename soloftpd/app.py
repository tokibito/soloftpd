from .server import Server
from .command import Command


class Application:
    command_class = Command
    server_class = Server

    def make_command(self):
        return self.command_class()

    def make_server(self, config):
        return self.server_class(config)

    def run(self, args=None):
        command = self.make_command()
        config = command.parse(args)
        server = self.make_server(config)
        server.start()


def main(application_class=Application):
    application = application_class()
    application.run()
    return application

if __name__ == '__main__':
    main()
