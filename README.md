# Flask Drop and Go Template

version 0.0.1 (alpha)

## Development

**Install dependencies**

**SYAFIK PLEASE CHECK THIS - I DON'T THINK IT'S NEEDED NOW

- Python 3.8.1 was tested
- Postgresql 10.3 was tested

1. Delete `peewee-db-evolve==3.7.0` from `requirements.txt` during the first installation.
   Because of how `peewee-db-evolve` created it's build process, we would first need to delete it.
1. Run:
   ```
   pip install -r requirements.txt
   ```
1. Now add `peewee-db-evolve==3.7.0` back into `requirements.txt`
1. Run again:
   ```
   pip install -r requirements.txt
   ```

If you're having trouble installing dependencies

- Remove `certifi==2018.11.29` from requirements.txt

If you're having trouble starting flask

- Restart your terminal as well and reactivate conda source

**Create a `.env` file at the root of the directory**

This project uses `python-dotenv`. When running commands using `flask`, environment variables from `.env` are automatically loaded.

When executing `python` scripts directly e.g. `python start.py`, environment variables are not loaded and will not work except `python migrate.py` _(read the script - `migrate.py` to know why it would load the environment variables `.env`)_

Minimum environment variables that needs to be set

```
FLASK_APP='start' # based on the name of our entry point script
FLASK_ENV='development' # use this in development, otherwise 'production' or 'test'
DATABASE_URL="postgres://localhost:5432/drop_and_go"
DB_TIMEOUT=300 # 5 minutes
DB_POOL=5

BRAINTREE KEYS

BT_MERCHANT_ID= #generate your own key
BT_PUBLIC_KEY= #generate your own key
BT_PRIVATE_KEY= #generate your own key

AWS KEYS (ACTUAL KEYS NOT YET REQUIRED)

S3_BUCKET_NAME= ''
S3_ACCESS_KEY_ID= ''
S3_SECRET_ACCESS_KEY= ''



```


Since this app uses Pooled Connections, you may also want to set:

```
DB_TIMEOUT=300 # 5 minutes
DB_POOL=5
```

_(see `database.py`)_

**Create a Database**

- this application is configured to use Postgresql

```
createdb nextagram_dev
```

_\*if you name your database something else, tweak the settings in `.env`_

**Ignoring Files from Git**

Before git commiting, remember to ignore key files. Here's an example of `.gitignore`

```
.vscode
*.DS_Store
*__pycache__
*.env
```

---

## Database Migrations

```
python migrate.py
```

\*_this template is configured to use Peewee's PooledConnection, however, migrations using Peewee-DB-Evolve doesn't work well. A hack was used to not use PooledConnection when running migration. Pending investigation. There are no known side effects to run this template in production._

## Starting Server

```
flask run
```

## Starting Shell

```
flask shell
```

---

## Deploying to Production

- ensure environment variables are configured appropriately
- migrations will not run in interactive mode when FLASK_ENV is set to 'production'

---

## Architecture

This template separates out API and Web to separate packages. Both API and Web are configured to use Flask's Blueprints.

All new models should go into it's own file/script within the models directory.

The entry point for a Flask server to start is located at `start.py`

---

## Dependencies

This code was created with `Python 3.8.1`.

`Peewee` is used as ORM along with a database migration library `peewee-db-evolve`.

A copy of requirements.txt is included in the repository.

```
certifi==2019.11.28
Click==7.0
colorama==0.4.3
Flask==1.1.1
Flask-Cors==3.0.8
itsdangerous==1.1.0
Jinja2==2.11.1
MarkupSafe==1.1.1
peewee==3.13.1
peewee-db-evolve==3.7.3
python-dotenv==0.10.5
six==1.14.0
Werkzeug==0.16.1
```

Remove `certifi==2018.11.28` if you're having trouble installing dependencies.

---
