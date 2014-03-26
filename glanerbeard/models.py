from ..core import db

shows_servers_relation_table = db.Table('shows_servers',
    db.Column('show_id', db.Integer, db.ForeignKey('show.id')),
    db.Column('server_id', db.Integer, db.ForeignKey('server.id'))
)

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255), unique=True)
    servers = db.relationship('Server', secondary=shows_servers_relation_table, backref=db.backref('shows', lazy='dynamic'))

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    sickbeard_url = db.Column(db.String(255), unique=True)
