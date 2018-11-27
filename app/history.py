# Blueprint for the history page

from flask import Blueprint, render_template, request, g
from app.database import get_db
from app.bug import get_bugs
from app.user import get_all_users
from app.status import get_all_statuses

bp = Blueprint('history', __name__, url_prefix='/history')

# Set up the history page endpoint, provides a list of bugs and statuses to build the page
@bp.route('/', methods=('GET',))
def get_dev_page():
	return render_template('history.html', bugs=get_bugs(), statuses=get_all_statuses())
