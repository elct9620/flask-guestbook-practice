Flask Guestbook Practice
===

My first Python CRUD project

### Requirements

* Python 3.6.12
* Pipenv

### Setup

Add `instance/config.py` to configure database and CSRF token

```py
# instance/config.py

SECRET_KEY = "DUMMY_KEY"
SQLALCHEMY_DATABASE_URI = "mysql://username:password@localhost/flask-guestbook"
```

Install dependencies via Pipenv


```bash
pipenv install
```

Run database migration


```bash
pipenv run flask db upgrade
```

Run Flask

```bash
pipenv run flask run
```
