import logging


class Show:
    def __init__(self, sb_id, sickbeard_json):
        self.name = sickbeard_json['show_name']
        self.sb_id = sb_id
        self.servers = set()

    def available_on(self, server):
        return server in self.servers

    def add_server(self, server):
        self.servers.add(server)

    def update(self, new_show):
        self.servers.update(new_show.servers)


def from_json(json):
    return [Show(sbid, definition) for sbid, definition in json['data'].items()]


def collect_from(servers):
    show_dict = {}
    success_servers = []
    for server in servers:
        try:
            for s in server.get_shows():
                if s.sb_id in show_dict:
                    show_dict[s.sb_id].update(s)
                else:
                    show_dict[s.sb_id] = s
            success_servers.append(server)
        except Exception as e:
            logging.warning(e)
    return success_servers, show_dict.values()
