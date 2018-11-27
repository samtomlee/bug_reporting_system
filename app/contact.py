from flask import Blueprint, render_template, request, g

bp = Blueprint('contact', __name__, url_prefix='/contact')

@bp.route('/', methods=('GET',))
def get_contact_page():
	return render_template('contact.html')
