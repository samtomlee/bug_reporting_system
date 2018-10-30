from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs

bp = Blueprint('manager', __name__, url_prefix='/manager')

@bp.route('/', methods=('GET',))
def get_dev_page():
	user = ''
	if 'user' in request.args.keys():
		user = request.args['user']
	
	# for testing, delete later
	else:
		user = 1
	
	return render_template('manager.html', bugs=get_bugs())