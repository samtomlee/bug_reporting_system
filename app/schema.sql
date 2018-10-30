-- Drop existing tables
DROP TABLE IF EXISTS bug;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS bugtype;

-- Create tables
CREATE TABLE bug (
	bug_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	status_id INTEGER NOT NULL,
	assignedmember_id INTEGER NOT NULL,
	bugtype_id INTEGER NOT NULL,
	submitter_email TEXT NOT NULL,
	submission_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(status_id) REFERENCES status(status_id),
	FOREIGN KEY(assignedmember_id) REFERENCES user(user_id),
	FOREIGN KEY(bugtype_id) REFERENCES bugtype(bugtype_id)
);

CREATE TABLE user (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	email TEXT NOT NULL
);

CREATE TABLE status (
	status_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE bugtype (
	bugtype_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

-- Add default data

INSERT INTO status (name)
VALUES
	("Submitted"),
	("Reproduced"),
	("Fixed"),
	("Tested"),
	("Closed");

INSERT INTO bugtype (name)
VALUES
	("eCampus"),
	("Camino"),
	("My SCU Portal"),
	("scu.edu");

INSERT INTO user (user_id, name, email)
VALUES
	(0, "unassigned", "unassigned");