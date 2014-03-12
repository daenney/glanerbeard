from flask import (
	Flask,
	render_template,
	abort
)

from server import Server
import logging

app = Flask(__name__)
app.config.from_pyfile('../settings.py')

servers = Server.createFromConfig(app.config['SERVERS'], app.config['API_KEYS'])

@app.route('/')
def index():
	shows = [server.getShows() for server in servers]
	return str(shows)


if __name__ == '__main__':
	app.debug = True
	app.run()
