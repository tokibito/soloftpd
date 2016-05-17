import json


class Config:
    address = "127.0.0.1"
    port = 21
    passive_ports = [30000, 50000]
    masquerade_address = None
    username = "spam"
    password = "egg"
    directory = "/tmp/"
    permission = "elradfmw"
    logging = {}

    def __init__(self, **kwargs):
        if kwargs:
            self.update(kwargs)

    def __setattr__(self, name, value):
        attr_name = name.replace('-', '_')
        if hasattr(self, attr_name):
            self.__dict__[attr_name] = value
        else:
            raise AttributeError("{} has no attribute: {}".format(self, name))

    def update(self, dic):
        for key, value in dic.items():
            setattr(self, key, value)

    @classmethod
    def from_file(cls, filepath):
        with open(filepath) as fp:
            config_dict = json.load(fp)
        return cls(**config_dict)
