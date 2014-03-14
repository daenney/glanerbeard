import requests
import logging
from glanerbeard import show
log = logging.getLogger(__name__)

class Server:
	def __init__(self, name, url, apikey):
		self.name = name
		self.url = url
		self.apikey = apikey

	def requestJson(self, path):
		url = '{url}/api/{apikey}{path}'.format(url=self.url,apikey=self.apikey,path=path)
		return requests.get(url, verify=False).json()

	def getShows(self):
		shows = show.fromJson(self.requestJson('/?cmd=shows'))
		for s in shows:
			s.addServer(self)
		return shows

	def __repr__(self):
		return 'Server {name} at {url}'.format(name=self.name,url=self.url)

def fromConfig(serverdict, apikeydict):
	result = []
	for name,url in serverdict.items():
		result.append(Server(name, url, apikeydict[name]))
	return result
