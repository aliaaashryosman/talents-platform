from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

# إنشاء المثيلات
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # تكوين التطبيق
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
    
    # تهيئة الإضافات
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    jwt.init_app(app)
    
    # التأكد من وجود مجلد التحميلات
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # تسجيل المسارات
    from app.routes import auth_bp, talents_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(talents_bp, url_prefix='/api/talents')
    
    # إنشاء قاعدة البيانات عند بدء التطبيق
    with app.app_context():
        db.create_all()
    
    @app.route('/test')
    def test_route():
        return {'message': 'API is working!'}
    
    return app