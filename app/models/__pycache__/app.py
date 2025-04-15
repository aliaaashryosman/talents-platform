# app.py
from flask import Flask
from models import db
from routes import auth_routes, project_routes, challenge_routes  # وغيرها من المسارات

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/talent_platform'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

# تهيئة قاعدة البيانات مع التطبيق
db.init_app(app)

# تسجيل مسارات API
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(project_routes, url_prefix='/api/projects')
app.register_blueprint(challenge_routes, url_prefix='/api/challenges')
# وهكذا لبقية المسارات

# إنشاء جميع الجداول عند تشغيل التطبيق
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)