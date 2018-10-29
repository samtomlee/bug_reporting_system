from .database import get_db

def get_status_id(name):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM status WHERE name=?', (name,)).fetchone()['status_id']

def get_status(status_id):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM status WHERE status_id=?', str(status_id)).fetchone()['name']