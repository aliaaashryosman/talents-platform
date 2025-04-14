from app import db
from datetime import datetime

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strengths = db.Column(db.Text)  # نقاط القوة
    weaknesses = db.Column(db.Text)  # نقاط الضعف
    score = db.Column(db.Float)  # التقييم العام (من 0 إلى 10)
    recommendations = db.Column(db.Text)  # التوصيات والاقتراحات
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign Keys
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    
    # العلاقات
    project = db.relationship('Project', backref=db.backref('analyses', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Analysis {self.id} for Project {self.project_id}>'