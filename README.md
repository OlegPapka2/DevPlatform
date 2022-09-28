# DevPlatform

This is collaborative platform for developers.

Chat and write code together.

## Developing

All example environmental variables could be found in [`.env.example`](./.env.example).

### How to start:

Create PostgreSQL db, and get your db url:

```bash
$ export DB_URL='postgresql://user_name:password@host:port/db_name'
```

Then run alembic revision and migration, to create all tables:

```bash
$ alembic revision --autogenerate -m 'initial'
$ alembic upgrade head
```
