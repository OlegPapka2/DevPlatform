from flask_migrate import Migrate, upgrade

from app import app, db


def create_tables():
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    with app.app_context():
        upgrade()


if __name__ == '__main__':
    create_tables()
