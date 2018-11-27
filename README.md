# Bug Reporting System
COEN 174 Lab Project: Creating a Bug Reporting System

## Setup
```sh
setup python3
python3 -m venv venv
. venv/bin/activate
pip install flask flask-login
export FLASK_APP=app
flask init-db
```

## Running
```sh
. venv/bin/activate
export FLASK_APP=app
flask run --host 0.0.0.0
```

## Accessing the website
\section{Accessing the website}
When the server is running on an SCU DC linux lab computer it can be accessed from any other lab computer using that computers hostname and the port 5000. Access the address linuxXXXXX.dc.engr.scu.edu:5000 with a browser to visit the website, replacing the X's with the lab computer's number. If you don't know the lab computer's number, type hostname into the terminal. To test authentication, the following accounts are available.

1. Manager
	* Username: mmanager@scu.edu
	* Password: mp@ssword
2. Tester
	* Username: ttesterson@scu.edu
	* Password: tp@ssword
3. Developer 1
	* Username: dguy@scu.edu
	* Password: dp@ssword
4. Developer 2
	* Username: dgal@scu.edu
	* Password: dp@ssword
