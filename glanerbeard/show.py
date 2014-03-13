class Show:
	def __init__(self, sb_id, sickbeard_json):
		self.name = sickbeard_json['show_name']
		self.sb_id = sb_id
		self.servers = set()	

	def availableOn(self, server):
		return server in self.servers

	def addServer(self, server):
		self.servers.add(server)

	def update(self, newShow):
		self.servers.update(newShow.servers)

def fromJson(json):
	return [Show(sbid, definition) for sbid, definition in json['data'].items()]
			
def collectFrom(servers):
	showdict = {}
	successServers = []
	for server in servers:
		try:
			for s in server.getShows():
				if s.sb_id in showdict:
					showdict[s.sb_id].update(s)
				else:
					showdict[s.sb_id] = s
			successServers.append(server)
		except Exception as e:
			# TODO log error
			pass
	return successServers, showdict.values()
