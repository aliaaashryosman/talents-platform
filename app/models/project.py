# from datetime import datetime
# from app import db

# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text)
#     file_path = db.Column(db.String(255))  # مسار الملف المرفوع
#     content = db.Column(db.Text)  # محتوى المشروع إذا تم إنشاؤه في الموقع
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     # Foreign Keys
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     talent_id = db.Column(db.Integer, db.ForeignKey('talent.id'), nullable=False)
    
#     # العلاقات
#     user = db.relationship('User', backref=db.backref('projects', lazy='dynamic'))
#     talent = db.relationship('Talent', backref=db.backref('projects', lazy='dynamic'))
    
#     def __repr__(self):
#         return f'<Project {self.title}>'


# الجزء التانى اللى تم ايقافه
# # models/project.py
# from datetime import datetime
# from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Text, Float
# from sqlalchemy.orm import relationship

# from . import db

# # جدول وسيط للعلاقة بين المشاريع والإعجابات
# project_likes = Table(
#     'project_likes', 
#     db.Model.metadata,
#     Column('project_id', Integer, ForeignKey('projects.id')),
#     Column('user_id', Integer, ForeignKey('users.id'))
# )

# class Project(db.Model):
#     __tablename__ = 'projects'
    
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), nullable=False)
#     description = Column(Text, nullable=False)
#     talent_type = Column(String(100), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
#     # العلاقات
#     user = relationship('User', backref='user_projects')
#     files = relationship('ProjectFile', back_populates='project')
#     likes = relationship('User', secondary=project_likes)
#     analyses = relationship('Analysis', back_populates='project')
    
#     # معلومات المشروع
#     thumbnail = Column(String(255))
#     is_public = Column(Boolean, default=True)
#     tags = Column(String(500))  # سيتم تخزينها كسلسلة مفصولة بفواصل
#     views = Column(Integer, default=0)
#     is_featured = Column(Boolean, default=False)
#     featured_date = Column(DateTime)
#     created_with_tool = Column(Boolean, default=False)
#     tool_id = Column(Integer, ForeignKey('tools.id'))
#     tool = relationship('Tool')
#     challenge_id = Column(Integer, ForeignKey('challenges.id'))
#     challenge = relationship('Challenge')
#     status = Column(String(20), default='published')
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     def __repr__(self):
#         return f'<Project {self.title}>'

# class ProjectFile(db.Model):
#     __tablename__ = 'project_files'
    
#     id = Column(Integer, primary_key=True)
#     project_id = Column(Integer, ForeignKey('projects.id'))
#     original_name = Column(String(255))
#     file_name = Column(String(255))
#     file_path = Column(String(500))
#     file_type = Column(String(100))
#     file_size = Column(Float)
#     upload_date = Column(DateTime, default=datetime.utcnow)
    
#     project = relationship('Project', back_populates='files')

from datetime import datetime
from . import db

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # العلاقات
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    talent_id = db.Column(db.Integer, db.ForeignKey('talents.id'))
    talent = db.relationship('Talent', backref='projects')
    
    def __repr__(self):
        return f'<Project {self.title}>'