from flask import Blueprint, render_template, request, g
#from app.database import get_db
#from app.bug import get_bugs
#from app.user import get_all_users
#from app.status import get_all_statuses

bp = Blueprint('faq', __name__, url_prefix='/faq')

@bp.route('/', methods=('GET',))
def get_faq_page():
	return render_template('faq.html')
