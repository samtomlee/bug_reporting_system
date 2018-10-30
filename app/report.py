from flask import Blueprint, render_template, request, g
from app.database import get_db

bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/', methods=('GET',))
def get_report_form():
	return render_template('form.html')

@bp.route('/', methods=('POST',))
def submit_bug_form():
	description = report.form.get('bugDesc')
	bug_type = report.form.get('typeBugs')
	submitter_email = report.form.get('')
