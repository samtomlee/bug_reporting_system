# Creates the Status model and provides functions to get statuses

from .database import get_db

# Status model
class Status:
	def __init__(self, status_id, name):
		self.id = status_id
		self.name = name

# Get a status' id from its name
def get_status_id(name):
	print(name)
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM status WHERE name=?', (name,)).fetchone()['status_id']

# Get a Status object from its id
def get_status(status_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM status WHERE status_id=?', str(status_id)).fetchone()
	return Status(data['status_id'], data['name'])

# Get a list of all Status objects
def get_all_statuses():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM status').fetchall()
	statuses = []
	for data in rows:
		statuses.append(Status(data['status_id'], data['name']))
	return statuses
