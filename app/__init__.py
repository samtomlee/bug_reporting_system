import os

from flask import Flask, redirect, url_for
from . import bug

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

	return app
