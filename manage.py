from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import app, db

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    '''Returns application and database instances
    to the shell importing them automatically
    on `python manager.py shell`.
    '''
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
