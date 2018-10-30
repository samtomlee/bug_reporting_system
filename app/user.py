from .database import get_db

class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email

def get_user_id_from_email(email):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM user WHERE email=?', (email,)).fetchone()['user_id']

def get_user(user_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM user WHERE user_id=?', (user_id,)).fetchone()
	return User(data['name'], data['email'])

def get_all_users():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM user').fetchall()
	users = []
	for data in rows:
		users.append(User(data['name'], data['email']))
	return users