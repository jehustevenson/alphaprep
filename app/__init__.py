from flask import Flask
from datetime import timedelta

#set up routes import
from .main.routes import main


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.DevelopmentConfig')
    
    #initialzing extensions
    with app.app_context():
        app.register_blueprint(main)
        
        
        app.permanent_session_lifetime = timedelta(minutes=300)	
    
    return app