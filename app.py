from flask import Flask, render_template, session
from flask_cas import CAS
from flask_cas import login
from flask_cas import logout
from flask_cas import login_required

app = Flask(__name__)
cas = CAS(app, '/cas')
app.config['CAS_SERVER'] = 'https://jasigcas.herokuapp.com' 
app.config['CAS_AFTER_LOGIN'] = 'secure'

@app.route("/secure")
@login_required
def secure():
    return render_template('secure.html')

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()