from datetime import datetime
from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(255))  # مسار الملف المرفوع
    content = db.Column(db.Text)  # محتوى المشروع إذا تم إنشاؤه في الموقع
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    talent_id = db.Column(db.Integer, db.ForeignKey('talent.id'), nullable=False)
    
    # العلاقات
    user = db.relationship('User', backref=db.backref('projects', lazy='dynamic'))
    talent = db.relationship('Talent', backref=db.backref('projects', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Project {self.title}>'