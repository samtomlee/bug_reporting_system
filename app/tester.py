from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs

bp = Blueprint('tester', __name__, url_prefix='/tester')

@bp.route('/<user_id>', methods=('GET',))
def get_dev_page(user_id):
	return render_template('tester.html', bugs=get_bugs({ 'assignedmember_id': user_id }))

@bp.route('/submit', methods=('POST',))
def submit_bug_change():
	data = request.get_json()
	bug_id = int(data['bug_id'])
	del data['bug_id']
	update_bug(bug_id, data)
	return "Bug updated"