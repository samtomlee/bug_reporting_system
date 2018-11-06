from .database import get_db

def get_severity_id(name):
	print(name)
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM severity WHERE name=?', (name,)).fetchone()['severity']

def get_severity(severity_id):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM severity WHERE severity_id=?', str(severity_id)).fetchone()['name']

def get_all_severities():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM severity').fetchall()
	severities = []
	for data in rows:
		severities.append(data['name'])
	return severities
