from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs
from app.user import get_all_users

bp = Blueprint('manager', __name__, url_prefix='/manager')

@bp.route('/<user_id>', methods=('GET',))
def get_dev_page(user_id):
	return render_template('manager.html', bugs=get_bugs(), assignees=get_all_users())