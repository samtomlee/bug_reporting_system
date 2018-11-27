from flask import Blueprint, render_template, request, g, session
from app.database import get_db
from app.bug import get_bugs
from app.status import get_all_statuses
from app.severity import get_all_severities

bp = Blueprint('tester', __name__, url_prefix='/tester')

@bp.route('/', methods=('GET',))
def get_dev_page_none():
	return render_template('not_found.html')

@bp.route('/<user_id>', methods=('GET',))
def get_dev_page(user_id):
	if(session.get('user_type') and session['user_type'] == "Tester"):
		return render_template('tester.html', bugs=get_bugs({ 'assignedmember_id': user_id }), severities=get_all_severities(), statuses=get_all_statuses())
	return render_template('not_found.html')

@bp.route('/submit', methods=('POST',))
def submit_bug_change():
	data = request.get_json()
	bug_id = int(data['bug_id'])
	del data['bug_id']
	update_bug(bug_id, data)
	return "Bug updated"
