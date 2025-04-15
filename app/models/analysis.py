# from app import db
# from datetime import datetime

# class Analysis(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     strengths = db.Column(db.Text)  # نقاط القوة
#     weaknesses = db.Column(db.Text)  # نقاط الضعف
#     score = db.Column(db.Float)  # التقييم العام (من 0 إلى 10)
#     recommendations = db.Column(db.Text)  # التوصيات والاقتراحات
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
#     # Foreign Keys
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    
#     # العلاقات
#     project = db.relationship('Project', backref=db.backref('analyses', lazy='dynamic'))
    
#     def __repr__(self):
#         return f'<Analysis {self.id} for Project {self.project_id}>'

from . import db

class Analysis(db.Model):
    __tablename__ = 'analyses'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    overall_score = db.Column(db.Float)
    
    # العلاقات
    strengths = db.relationship('AnalysisStrength', backref='analysis')
    weaknesses = db.relationship('AnalysisWeakness', backref='analysis')
    criteria = db.relationship('AnalysisCriteria', backref='analysis')

class AnalysisStrength(db.Model):
    __tablename__ = 'analysis_strengths'
    
    id = db.Column(db.Integer, primary_key=True)
    analysis_id = db.Column(db.Integer, db.ForeignKey('analyses.id'))
    description = db.Column(db.String(500))
    score = db.Column(db.Float)

class AnalysisWeakness(db.Model):
    __tablename__ = 'analysis_weaknesses'
    
    id = db.Column(db.Integer, primary_key=True)
    analysis_id = db.Column(db.Integer, db.ForeignKey('analyses.id'))
    description = db.Column(db.String(500))
    score = db.Column(db.Float)

class AnalysisCriteria(db.Model):
    __tablename__ = 'analysis_criteria'
    
    id = db.Column(db.Integer, primary_key=True)
    analysis_id = db.Column(db.Integer, db.ForeignKey('analyses.id'))
    name = db.Column(db.String(100))
    score = db.Column(db.Float)
    weight = db.Column(db.Float)