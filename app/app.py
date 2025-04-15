# app.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()



from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models import user, talent, project, analysis
    from app.routes import auth, talents
    
    return app