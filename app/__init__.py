# This file contains the function used to initialise the application


import os

from flask import Flask, redirect, url_for, request, render_template, session
from . import bug
import flask_login
# import hashlib

# create_app is called to initialise the application. It loads configuration information,
# gives the app database information, and registers all of the web pages. It also
# sets up small webpages that need little code like the home page, login and logout.

# Parameters:
# 	test_config (defaults to None) - if not None test_config will be used in place of a config file
# Returns: app object
def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = '?[Bz_?ٮ??`&?W[',
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

	@app.route('/report')
	def get_report_form():
		return render_template('form.html')


	@app.route('/')
	def get_home():
		return render_template('home.html')

	@app.route('/contact')
	def get_contact_page():
		return render_template('contact.html')

	@app.route('/faq')
	def get_faq_page():
		return render_template('faq.html')

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

	# login functionality

	login_manager = flask_login.LoginManager()
	login_manager.init_app(app)

	# login page
	# If the request is a POST request then the user
	# is trying to authenticate, if it is a GET request
	# then just provide the login page
	@app.route('/login', methods=['GET', 'POST'])
	def login():
		from app.login import validate
		error = None
		if request.method == 'POST':
			isValid, id_user, type_user = validate(request.form['username'], request.form['password'])
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

	# logout page
	# logs out the user and redirects to the bug report page
	@app.route('/logout')
	def logout():
		session.pop('logged_in', None)
		session.pop('user_type', None)
		session.pop('user_url', None)
		return redirect('/report')

	if __name__== "__main__":
		app.run()

	return app
