from flask import Blueprint, render_template, request, g, session
from app.database import get_db
from app.bug import get_bugs
from app.user import get_non_managers
from app.status import get_all_statuses

bp = Blueprint('manager', __name__, url_prefix='/manager')

@bp.route('/', methods=('GET',))
def get_manage_page_none():
	return render_template('not_found.html')

@bp.route('/<user_id>', methods=('GET',))
def get_manage_page(user_id):
	if(session.get('user_type') and session['user_type'] == "Manager"):
		return render_template('manager.html', bugs=get_bugs(), assignees=get_non_managers(), statuses=get_all_statuses())
	return render_template('not_found.html')
