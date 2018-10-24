import sqlite3
from flask import Flask, g
app = Flask(__name__)


@app.route('/')
def hello_world():
	for status in query_db('select * from statuses'):
		print(status['name'])
	return 'Hello, world!'


DATABASE = 'database.db'

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)

	db.row_factory = sqlite3.Row
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
