import requests

from glanerbeard import show, settings


class Server:
    def __init__(self, name, url, apikey):
        self.name = name
        self.url = url
        self.apikey = apikey

    def request_json(self, path):
        url = '{url}/api/{apikey}{path}'.format(url=self.url, apikey=self.apikey, path=path)
        return requests.get(url, verify=settings['SSL_VERIFY']).json()

    def get_shows(self):
        shows = show.from_json(self.request_json('/?cmd=shows'))
        for s in shows:
            s.add_server(self)
        return shows

    def __repr__(self):
        return 'Server {name} at {url}'.format(name=self.name, url=self.url)


def fromConfig(serverdict, apikeydict):
    result = []
    for name, url in serverdict.items():
        result.append(Server(name, url, apikeydict[name]))
    return result
