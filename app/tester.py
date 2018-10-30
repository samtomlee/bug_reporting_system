from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs

bp = Blueprint('tester', __name__, url_prefix='/tester')

@bp.route('/', methods=('GET',))
def get_dev_page():
	user = ''
	if 'user' in request.args.keys():
		user = request.args['user']
	
	# for testing, delete later
	else:
		user = 1
	
	return render_template('tester.html', bugs=get_bugs({ 'assignedmember_id': user }))