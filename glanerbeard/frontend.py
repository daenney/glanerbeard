import logging
from flask import Blueprint, render_template, current_app


frontend = Blueprint('frontend', __name__, template_folder='templates')
log = logging.getLogger(__name__)

@frontend.route('/')
def index():
    (queried_servers, shows) = show.fetch_all()
    return render_template('show_status.html', shows=shows, servers=queried_servers)
