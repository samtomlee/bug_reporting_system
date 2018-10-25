from .database import get_db

def get_bug_type_id(name):
	db = get_db()	
	return db.execute('SELECT * FROM bugtype WHERE name=?', name).fetchone()['bugtype_id']

def get_bug_type(bug_type_id):
	db = get_db()
	return db.execute('SELECT * FROM bugtype WHERE bugtype_id=?', bug_type_id).fetchone()['name']