from .database import get_db
from .status import get_status_id, get_status
from .bug_type import get_bug_type_id, get_bug_type
from .user import get_user_id_from_email, get_user

class Bug:
	def __init__(self, bug_id, description, status_id, user_id, bug_type_id, submitter_email, submission_time):
		self.id = bug_id
		self.description = description
		self.status = get_status(status_id)
		self.assigned_member = get_user(user_id)
		self.bug_type = get_bug_type(bug_type_id)
		self.submitter_email = submitter_email
		self.submission_time = submission_time

def create_bug(description, status, assigned_member, bug_type, submitter_email):
	db = get_db()
	cur = db.cursor()

	status_id = get_status_id(status)
	type_id = get_bug_type_id(bugtype)
	user_id = get_user_id_from_email(assigned_member)

	cur.execute(
		"""
		INSERT INTO bug (description, status_id, assignedmember_id, bugtype_id, submitter_email)
		VALUES (?, ?, ?, ?, ?, ?)
		""",
		(description, str(status_id), str(user_id), str(type_id), submitter_email)
		)
	db.commit()

def get_bug(bug_id):
	cur = get_db().cursor()
	data = cur.execute('SELECT * FROM bug WHERE bug_id=?', ((bug_id),)).fetchone()
	return Bug(data['bug_id'], data['description'], data['status_id'], data['assignedmember_id'], data['bugtype_id'], data['submitter_email'], data['submission_time'])

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
		bugs.append(Bug(data['bug_id'], data['description'], data['status_id'], data['assignedmember_id'], data['bugtype_id'], data['submitter_email'], data['submission_time']))

	return bugs

def update_bug(bug_id, new_data):
	db = get_db()
	cur = db.cursor()

	query = "UPDATE bug SET"

	if 'status' in new_data.keys():
		new_data['status_id'] = get_status_id(new_data['status'])
		del new_data['status']

	if 'assigned_member' in new_data.keys():
		new_data['user_id'] = get_user_id_from_email(new_data['assigned_member'])
		del new_data['assigned_member']

	values = []
	for key, value in new_data.items():
		query += " {}=?,".format(key)
		values.append(value)

	query = query[:-1]
	query += " WHERE bug_id=?"
	values.append(bug_id)

	print(query)
	print(values)
	cur.execute(query, values)
	db.commit()