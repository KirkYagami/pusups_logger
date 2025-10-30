"""
 When we run Flask app using the flask run command, Flask looks for a function named create_app (or app) in your module by default.
 --> application factory (a callable that returns a Flask app instance).
"""


from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)




    return app