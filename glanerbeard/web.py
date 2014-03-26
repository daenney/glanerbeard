import logging
import json

from flask import (
    Flask,
    render_template
)

from glanerbeard import server, show, settings


def json_print(value):
    return json.dumps(value, indent=2, separators=(',', ': '))


app = Flask(__name__)
settings.init(app)
app.jinja_env.filters['json_print'] = json_print

numeric_level = getattr(logging, settings['LOGLEVEL'].upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % numeric_level)
logging.basicConfig(level=numeric_level)
log = logging.getLogger(__name__)

servers = server.fromConfig(settings['SERVERS'], settings['API_KEYS'])


@app.route('/')
def index():
    (queried_servers, shows) = show.collect_from(servers)
    return render_template('show_status.html', shows=shows, servers=queried_servers)
