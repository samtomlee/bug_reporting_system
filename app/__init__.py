import os

from flask import Flask, redirect, url_for, request, render_template, session, flash
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

	from app.database import get_db
	#login functionality
	def check_password(hashed_password, user_password):
		return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

	def validate(username, password):
		#how to access the user database?
		con = get_db()
		completion = False
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM user")
			rows = cur.fetchall()
			for row in rows:
				dbUser = row[0]
				dbPass = row[1]
				if dbUser==username:
					completion=check_password(dbPass, password)
					return completion

	login_manager = flask_login.LoginManager()
	login_manager.init_app(app)

	@app.route('/login', methods=['GET', 'POST'])
	def login():
		error = None
		if request.method == 'POST':
			if(validate(request.form['username'], request.form['password']) == False):
				error = 'Invalid Credentials. Please try again.'
			else:
				session['logged_in'] = True
				flash('You were logged in.')
				return redirect('/history')
		return render_template('login.html', error=error)


	@app.route('/logout')
	#@login_required <-- look into this tag
	def logout():
		session.pop('logged_in', None)
		flash('You were logged out.')
		return redirect('/report')

	if __name__== "__main__":
		app.run()

	return app
