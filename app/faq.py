from flask import Blueprint, render_template, request, g

bp = Blueprint('faq', __name__, url_prefix='/faq')

@bp.route('/', methods=('GET',))
def get_dev_page():
	return render_template('faq.html')
