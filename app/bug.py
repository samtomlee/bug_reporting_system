from .database import get_db
from .status import get_status_id, get_status
from .severity import get_severity_id, get_severity
from .bug_type import get_bug_type_id, get_bug_type
from .user import get_user_id_from_email, get_user
from flask import Blueprint, request, jsonify

bp = Blueprint('bug', __name__, url_prefix='/bug')

class Bug:
	def __init__(self, data):
		self.id = data['bug_id']
		self.name = data['name']
		self.description = data['description']
		self.status = get_status(data['status_id'])
		self.assigned_member = get_user(data['assignedmember_id'])
		self.type = get_bug_type(data['bugtype_id'])
		self.severity = get_severity(data['severity_id'])
		self.submitter_email = data['submitter_email']
		self.submission_time = data['submission_time']
		self.last_updated = data['last_updated']

def create_bug(name, description, status, bug_type, submitter_email):
	db = get_db()
	cur = db.cursor()

	status_id = get_status_id(status)
	type_id = get_bug_type_id(bug_type)

	cur.execute(
		"""
		INSERT INTO bug (name, description, status_id, assignedmember_id, bugtype_id, severity_id, submitter_email)
		VALUES (?, ?, ?, ?, ?, ?, ?)
		""",
		(name, description, status_id, 0, type_id, 1, submitter_email)
		)
	db.commit()

def get_bug(bug_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM bug WHERE bug_id=?', ((bug_id),)).fetchone()
	return Bug(data)

def get_bugs(filters = {}):
	cur = get_db().cursor()
	query = "SELECT * FROM bug"

	i = 0
	values = []
	for key, value in filters.items():
		if i == 0:
			query += " WHERE {}=?".format(key)
			values.append(value)
		else:
			query += " AND {}=?".format(key)
			values.append(value)
		i += 1

	rows = cur.execute(query, values).fetchall()
	bugs = []
	for data in rows:
		bugs.append(Bug(data))

	return bugs

def update_bug(bug_id, new_data):
	db = get_db()
	cur = db.cursor()

	query = "UPDATE bug SET"

	if 'status' in new_data.keys():
		new_data['status_id'] = get_status_id(new_data['status'])
		del new_data['status']

	if 'assigned_member' in new_data.keys():
		new_data['assignedmember_id'] = get_user_id_from_email(new_data['assigned_member'])
		del new_data['assigned_member']

	if 'severity' in new_data.keys():
		new_data['severity_id'] = get_severity_id(new_data['severity'])
		del new_data['severity']


	values = []
	for key, value in new_data.items():
		query += " {}=?,".format(key)
		values.append(value)

	query += " last_updated=CURRENT_TIMESTAMP "

	query += " WHERE bug_id=?"
	values.append(bug_id)

	print(query)
	print(values)
	cur.execute(query, values)
	db.commit()

@bp.route('/update', methods=('POST',))
def submit_bug_change():
	data = request.get_json()
	bug_id = int(data['bug_id'])
	del data['bug_id']
	update_bug(bug_id, data)
	return "Bug updated"

@bp.route('/create', methods=('POST',))
def submit_bug_form():
	data = request.get_json()
	create_bug(data['name'], data['description'], 'Submitted', data['bugtype'], data['email'])
	return "Bug report submitted"

@bp.route('/search', methods=('POST',))
def request_bug():
	data = request.get_json()
	bugs = get_bugs(data)
	return jsonify(bugs)