from flask import Blueprint, render_template, request, g
from app import app
#from app.database import get_db
#from app.bug import get_bugs
#from app.user import get_all_users
#from app.status import get_all_statuses

bp = Blueprint('login', __name__, url_prefix='/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

def validate(username, password):
    con = DATABASE
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
	return hashed_password == hashlib.md5(user_password.encode()).hexdigest()
