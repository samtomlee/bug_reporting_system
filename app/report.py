from flask import Blueprint, render_template, request, redirect, url_for, g
from app.bug import create_bug

bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/', methods=('GET',))
def get_report_form():
	return render_template('form.html')

@bp.route('/submit', methods=('POST',))
def submit_bug_form():
	data = request.get_json()
	create_bug(data['name'], data['description'], 'Submitted', data['bugtype'], data['email'])
	return redirect(url_for('report.get_report_form'))