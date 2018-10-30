from flask import Blueprint, render_template, request, redirect, url_for, g, Flask
from app.bug import create_bug

app = Flask(__name__)
bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/', methods=('GET',))
def get_report_form():
	return render_template('form.html')
