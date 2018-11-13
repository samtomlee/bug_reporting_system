-- Drop existing tables
DROP TABLE IF EXISTS bug;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS bugtype;
DROP TABLE IF EXISTS severity;
DROP TABLE IF EXISTS usertype;

-- Create tables
CREATE TABLE bug (
	bug_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	status_id INTEGER NOT NULL,
	assignedmember_id INTEGER NOT NULL,
	bugtype_id INTEGER NOT NULL,
	severity_id INTEGER NOT NULL,
	submitter_email TEXT NOT NULL,
	submission_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY(status_id) REFERENCES status(status_id),
	FOREIGN KEY(assignedmember_id) REFERENCES user(user_id),
	FOREIGN KEY(bugtype_id) REFERENCES bugtype(bugtype_id),
	FOREIGN KEY(severity_id) REFERENCES severity(severity_id)
);

CREATE TABLE user (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL,
	usertype_id INTEGER NOT NULL,
	FOREIGN KEY(usertype_id) REFERENCES usertype(usertype_id)
);

CREATE TABLE status (
	status_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE bugtype (
	bugtype_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE severity(
	severity_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE usertype(
	usertype_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
	("MySCU Portal"),
	("scu.edu");

INSERT INTO severity (name)
VALUES
	("Unset"),
	("Low"),
	("Medium"),
	("High");

INSERT INTO user (user_id, name, email, password, usertype_id)
VALUES
	(0, "Unassigned", "Unassigned", "", 0),
	(1, "Manny Manager", "mmanager@scu.edu", "mp@ssword", 1),
	(2, "Test Testerson", "ttesterson@scu.edu", "tp@ssword", 2),
	(3, "Dev Guy", "dguy@scu.edu", "dp@ssword", 3),
	(4, "Dev Gal", "dgal@scu.edu", "dp@ssword", 3);

INSERT INTO usertype (name)
VALUES
	("Manager"),
	("Tester"),
	("Developer");
