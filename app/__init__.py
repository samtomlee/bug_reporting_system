import os

from flask import Flask, redirect, url_for, request, render_template, session
from . import bug
import flask_login
import hashlib

def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'supersecret',
		DATABASE = os.path.join(app.instance_path, 'db.sqlite'),
	)

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import database
	database.init_app(app)

	from . import report
	app.register_blueprint(report.bp)

	@app.route('/')
	def home_redirect():
		return redirect(url_for('report.get_report_form'))

	from . import developer
	app.register_blueprint(developer.bp)

	from . import tester
	app.register_blueprint(tester.bp)

	from . import manager
	app.register_blueprint(manager.bp)

	from . import bug
	app.register_blueprint(bug.bp)

	from . import history
	app.register_blueprint(history.bp)

	from . import home
	app.register_blueprint(home.bp)

	from . import faq
	app.register_blueprint(faq.bp)

	# login functionality
	from app.database import get_db
	from app.user import get_user_type, get_user_type_from_email, get_user_id_from_email

	def check_password(hashed_password, user_password):
		return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

	def validate(username, password):
		#how to access the user database?
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

	login_manager = flask_login.LoginManager()
	login_manager.init_app(app)

	@app.route('/login', methods=['GET', 'POST'])
	def login():
		error = None
		if request.method == 'POST':
			isValid, id_user, type_user = validate(request.form['username'], request.form['password'])
			# isValid = validate(request.form['username'], request.form['password'])
			# id_user = 1
			if(isValid == False):
				error = 'Invalid Credentials. Please try again.'
			else:
				session['logged_in'] = True
				session['user_type'] = type_user
				user = str(id_user)
				nextUrl = ('/' + type_user.lower() + '/' + user)
				session['user_url'] = nextUrl
				return redirect(nextUrl)
		return render_template('login.html', error=error)


	@app.route('/logout')
	#@login_required <-- look into this tag?
	def logout():
		session.pop('logged_in', None)
		session.pop('user_type', None)
		session.pop('user_url', None)
		return redirect('/report')

	if __name__== "__main__":
		app.run()

	return app
