from flask import Blueprint, render_template, request, g, session
from app.database import get_db
from app.bug import get_bugs
from app.status import get_all_statuses
from app.severity import get_all_severities

bp = Blueprint('tester', __name__, url_prefix='/tester')

# Create endpoint for the user page using its id
@bp.route('/<user_id>', methods=('GET',))
def get_dev_page(user_id):
	if(session.get('user_type') and session['user_type'] == "Tester"):
		return render_template('tester.html', bugs=get_bugs({ 'assignedmember_id': user_id }), severities=get_all_severities(), statuses=get_all_statuses())
	return render_template('not_found.html')