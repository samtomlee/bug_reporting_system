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

	status_id = get_status_id(status)
	type_id = get_bug_type_id(bugtype)
	user_id = get_user_id_from_email(assigned_member)

	db.execute(
		"""
		INSERT INTO bug (description, status_id, assignedmember_id, bugtype_id, submitter_email)
		VALUES (?, ?, ?, ?, ?, ?)
		""",
		(description, status_id, user_id, type_id, submitter_email)
		)
	db.commit()

def get_bug(bug_id):
	db = get_db()
	data = db.execute('SELECT * FROM bug WHERE bug_id=?', (bug_id,)).fetchone()
	return data.keys()
