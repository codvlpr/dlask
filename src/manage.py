import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from app import app, db
from models import *

app.config.from_object(os.getenv("APP_SETTINGS", "config.DevConfig"))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()