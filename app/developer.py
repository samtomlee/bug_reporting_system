from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs, update_bug

bp = Blueprint('dev', __name__, url_prefix='/developer')

@bp.route('/<user_id>', methods=('GET',))
def get_dev_page(user_id):
	return render_template('developer.html', bugs=get_bugs({ 'assignedmember_id': user_id }))