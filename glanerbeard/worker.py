from . import server


class Worker():
    def __init__(self, config):
        self.config = config
        self.servers = server.from_config(config['SERVERS'], config['API_KEYS'])