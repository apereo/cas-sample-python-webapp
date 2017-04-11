# Overview

This is a sample Python web application using Flask that is protected via an Apereo CAS server using the [Flask CAS extension](https://github.com/cameronbwhite/Flask-CAS).

# Requirements

- Python

```bash
$ python --version
Python 2.7.10
```

- Pip

```bash
$ pip --version
pip 9.0.1 from /Library/Python/2.7/site-packages (python 2.7)
```

# Flask CAS Extension

You *may* need to download/install the CAS Flask extension from source locally to obtain a bug fix that helps with CAS attribute parsing. The bug fix, as of this writing, is not yet released.

```bash
git clone git@github.com:cameronbwhite/Flask-CAS.git
cd Flask-CAS
sudo python setup.py install
```

If you wish to not install plugin from source, simply execute:

```bash
pip install Flask-CAS
```

# Run

```bash
python app.py

...

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 120-601-740
```

# Test

Navigate to `http://localhost:5000` and click on the login button.
You will be redirected to a CAS server to authenticate and once you return,
you should see the authenticated user id plus any and all attributes that
the server may have authorized you to receive.

# Configuration

CAS configuration may be specified in `app.py`:

```python
app.config['CAS_SERVER'] = 'https://jasigcas.herokuapp.com' 
app.config['CAS_AFTER_LOGIN'] = 'secure'
```

For all other relevant settings, please refer to the [Flask CAS extension](https://github.com/cameronbwhite/Flask-CAS) project.