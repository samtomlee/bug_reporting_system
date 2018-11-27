# Contains functions to help with login

from flask import render_template, request, g

# login functionality
from app.database import get_db
from app.user import get_user_type, get_user_type_from_email, get_user_id_from_email
import flask_login
import hashlib

# Compares the hashed password from the database to the provided password
# Parameter:
#	hashed_password (string) - hashed password from the database
#	user_password (string) - user provided password
# Returns: True if the user's password matches the hashed one when hashed, False otherwise
def check_password(hashed_password, user_password):
	return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

# Validates a user's login
# Parameters:
#	username (string) - the user's username
#	password (string) - the user's password
# Returns: a 3-tuple with a boolean indicating if the validation was successful,
#	the id of the user, and the type of the user
def validate(username, password):
	con = get_db()
	completion = False
	id_user = 0
	type_user = 0
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM user")
		rows = cur.fetchall()
		for row in rows:
			dbUser = row[2]
			dbPass = row[3]
			if dbUser==username:
				completion=check_password(dbPass, password)
				if completion:
					id_user=get_user_id_from_email(username)
					type_user=get_user_type_from_email(username)
	return (completion, id_user, type_user)
