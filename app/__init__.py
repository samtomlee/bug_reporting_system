import os

from flask import Flask, redirect, url_for, request, render_template, session
from . import bug
import flask_login
# import hashlib

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

	from . import faq
	app.register_blueprint(faq.bp)

	login_manager = flask_login.LoginManager()
	login_manager.init_app(app)

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
