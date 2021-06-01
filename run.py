from app import create_app
from flask_script import Server, Manager


def _make_context():
    return dict(app=create_app)


manager = Manager(create_app)
manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()