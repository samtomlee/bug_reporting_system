import os

from flask import Flask, redirect, url_for, render_template, flash
from . import bug
from flask_login import LoginManager
from app.loginform import LoginForm

def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'supersecret',
		DATABASE = os.path.join(app.instance_path, 'db.sqlite'),
	)

	login = LoginManager(app)

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
		# if the session user is not signed in
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

	@app.route('/login', methods=['GET', 'POST'])
	def login():
	    if current_user.is_authenticated:
	        return redirect(url_for('/'))
	    form = LoginForm()
	    if form.validate_on_submit():
	        user = User.query.filter_by(username=form.username.data).first()
	        if user is None or not user.check_password(form.password.data):
	            flash('Invalid username or password')
	            return redirect(url_for('login'))
	        login_user(user, remember=form.remember_me.data)
	        return redirect(url_for('/'))
	    return render_template('login.html', title='Sign In', form=form)

	@app.route('/logout')
	def logout():
	    logout_user()
	    return redirect(url_for('index'))

	return app
