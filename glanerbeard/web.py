import logging

from flask import (
	Flask,
	render_template,
	abort
)

from glanerbeard.server import Server

app = Flask(__name__)
app.config.from_object('glanerbeard.default_settings')
app.config.from_envvar('GLANERBEARD_SETTINGS')

numeric_level = getattr(logging, app.config['LOGLEVEL'].upper(), None)
if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level)
log = logging.getLogger(__name__)

servers = Server.createFromConfig(app.config['SERVERS'], app.config['API_KEYS'])

@app.route('/')
def index():
	shows = [server.getShows() for server in servers]
	return str(shows)


if __name__ == '__main__':
	app.debug = True
	app.run()
