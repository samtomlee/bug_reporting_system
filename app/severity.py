from .database import get_db

class Severity:
	def __init__(self, severity_id, name):
		self.id = severity_id
		self.name = name

def get_severity_id(name):
	print(name)
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM severity WHERE name=?', (name,)).fetchone()['severity_id']

def get_severity(severity_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM severity WHERE severity_id=?', str(severity_id)).fetchone()
	return Severity(data['severity_id'], data['name'])

def get_all_severities():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM severity').fetchall()
	severities = []
	for data in rows:
		severities.append(Severity(data['severity_id'], data['name']))
	return severities
