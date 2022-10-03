# DevPlatform

This is collaborative platform for developers. Chat and write code together.

## Developing

All example environmental variables could be found in [`.env.example`](./.env.example).

### How to run migrations:

Create PostgreSQL db, and get your db url:

```bash
$ export DB_URL='postgresql://user_name:password@host:port/db_name'
```

Then run alembic revision and migration, to create all tables:

```bash
$ alembic revision --autogenerate -m 'initial'
$ alembic upgrade head
```

### How to run app:

Runs app on default path `http://127.0.0.1:5000/`.

```bash
$ python3 -m flask --app src/app run
# or for Windows
$ py -m flask --app src/app run
```

As always PyCharm simplifies our being, look 
[here](https://flask.palletsprojects.com/en/2.2.x/cli/#pycharm-integration) for details.  
Do not forget to specify app location via `--app src/app`.