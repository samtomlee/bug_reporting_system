from .database import get_db

def get_status_id(name):
	print(name)
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM status WHERE name=?', (name,)).fetchone()['status_id']

def get_status(status_id):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM status WHERE status_id=?', str(status_id)).fetchone()['name']

def get_all_statuses():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM status').fetchall()
	statuses = []
	for data in rows:
		statuses.append(data['name'])
	return statuses
