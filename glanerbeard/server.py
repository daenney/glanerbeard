import requests
import logging
log = logging.getLogger(__name__)

class Server:
	def __init__(self, name, url, apikey):
		self.name = name
		self.url = url
		self.apikey = apikey

	def requestJson(self, path):
		return requests.get('{url}/api/{apikey}{path}'.format(url=self.url,apikey=self.apikey,path=path)).json()

	def getShows(self):
		return self.requestJson('/?cmd=shows')

	def __repr__(self):
		return 'Server {name} at {url}'.format(name=self.name,url=self.url)

	@staticmethod
	def createFromConfig(serverdict, apikeydict):
		result = []
		for name,url in serverdict.items():
			result.append(Server(name, url, apikeydict[name]))
		return result
