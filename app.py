from os import path, getcwd
from sys import argv

from flask import Flask, render_template, session, redirect, send_from_directory
from flask_cas import CAS
from flask_cas import login
from flask_cas import logout
from flask_cas import login_required
import logging

app = Flask(__name__)
cas = CAS(app, '/cas')
app.config['CAS_SERVER'] = 'https://casserver.herokuapp.com'
app.config['CAS_AFTER_LOGIN'] = 'secure'
# app.config['CAS_LOGOUT_ROUTE'] =
# app.config['CAS_VALIDATE_ROUTE'] =
# app.config['CAS_VALIDATE_ROUTE'] =


@app.route("/logout")
def logout():
    session.clear()
    return render_template('logout.html')


@app.route("/secure")
@login_required
def secure():
    username = cas.username
    attributes = cas.attributes

    logging.info('CAS username: %s', username)
    logging.info('CAS attributes: %s', attributes)

    return render_template('secure.html', cas=cas)


@app.route("/caslogout")
def caslogout():
    return redirect(app.config['CAS_LOGOUT_ROUTE'], code=302)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(path.join(getcwd(), 'static'), filename)


if __name__ == "__main__":
    if len(argv) >= 3 and argv[1] == '--server':
        app.config['CAS_SERVER'] = argv[2]

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
