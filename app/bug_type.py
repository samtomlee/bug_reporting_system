# Provides functions to work with bug types

from .database import get_db

# Gets the id of a bug type from its name
def get_bug_type_id(name):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM bugtype WHERE name=?', (name,)).fetchone()['bugtype_id']

# Gets the name of a bug type from its id
def get_bug_type(bug_type_id):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM bugtype WHERE bugtype_id=?', (bug_type_id,)).fetchone()['name']