from .database import get_db

class Status:
	def __init__(self, status_id, name):
		self.id = status_id
		self.name = name

def get_status_id(name):
	print(name)
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM status WHERE name=?', (name,)).fetchone()['status_id']

def get_status(status_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM status WHERE status_id=?', str(status_id)).fetchone()
	return Status(data['status_id'], data['name'])

def get_all_statuses():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM status').fetchall()
	statuses = []
	for data in rows:
		statuses.append(Status(data['status_id'], data['name']))
	return statuses
