from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs, update_bug
from app.status import get_all_statuses
from app.severity import get_all_severities

bp = Blueprint('dev', __name__, url_prefix='/developer')

@bp.route('/<user_id>', methods=('GET',))
def get_dev_page(user_id):
	return render_template('developer.html', bugs=get_bugs({ 'assignedmember_id': user_id }), statuses=get_all_statuses(), severities=get_all_severities())
