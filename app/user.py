from .database import get_db

class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email

def get_user_id_from_email(email):
	db = get_db()	
	return db.execute('SELECT * FROM user WHERE email=?', email).fetchone()['user_id']

def get_user(user_id):
	db = get_db()
	data = db.execute('SELECT * FROM user WHERE user_id=?', str(user_id)).fetchone()
	return User(data['name'], data['email'])