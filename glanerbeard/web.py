import logging
import json

from flask import (
	Flask,
	render_template,
	abort
)

from glanerbeard import server, show

def jsonprint(value):
  return json.dumps(value, indent=2, separators=(',', ': ') )

app = Flask(__name__)
app.config.from_object('glanerbeard.default_settings')
app.config.from_envvar('GLANERBEARD_SETTINGS')
app.jinja_env.filters['jsonprint'] = jsonprint

numeric_level = getattr(logging, app.config['LOGLEVEL'].upper(), None)
if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level)
log = logging.getLogger(__name__)

servers = server.fromConfig(app.config['SERVERS'], app.config['API_KEYS'])

@app.route('/')
def index():
	(queriedServers, shows) = show.collectFrom(servers)
	return render_template('showstatus.html', shows=shows, servers=queriedServers)
