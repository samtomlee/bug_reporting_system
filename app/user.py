from .database import get_db

class User:
	def __init__(self, name, email, password, usertype_id):
		self.name = name
		self.email = email
		self.password = password
		self.usertype_id = usertype_id

def get_user_type_id(name):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM usertype WHERE name=?', (name,)).fetchone()['usertype_id']

def get_user_type_from_email(email):
	cur = get_db().cursor()
	user = get_user_from_email(email)
	return get_user_type(user.usertype_id)

def get_user_type(user_type_id):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM usertype WHERE usertype_id=?', (user_type_id,)).fetchone()['name']

def get_user_id_from_email(email):
	cur = get_db().cursor()
	return cur.execute('SELECT * FROM user WHERE email=?', (email,)).fetchone()['user_id']

def get_user_from_email(email):
	cur = get_db().cursor()
	id = get_user_id_from_email(email)
	return get_user(id)

def get_user(user_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM user WHERE user_id=?', (user_id,)).fetchone()
	return User(data['name'], data['email'], data['password'], data['usertype_id'])

def get_all_users():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM user').fetchall()
	users = []
	for data in rows:
		users.append(User(data['name'], data['email'], data['password'], data['usertype_id']))
	return users

def get_non_managers():
	cur = get_db().cursor()
	rows = cur.execute('SELECT * FROM user WHERE usertype_id!=?', (get_user_type_id("Manager"),)).fetchall()
	users = []
	for data in rows:
		users.append(User(data['name'], data['email'], data['password'], data['usertype_id']))
	return users
