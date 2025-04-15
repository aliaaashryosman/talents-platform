# from datetime import datetime
# from app import db
# from werkzeug.security import generate_password_hash, check_password_hash

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
        
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
    
#     def __repr__(self):
#         return f'<User {self.username}>'



# # ده تانى جزى تم ايقافه 
# # models/user.py
# from datetime import datetime
# from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Float, Text
# from sqlalchemy.orm import relationship
# from werkzeug.security import generate_password_hash, check_password_hash

# from . import db  # استيراد كائن قاعدة البيانات

# # جدول وسيط للعلاقة بين المستخدمين والتحديات المكتملة
# user_completed_challenges = Table(
#     'user_completed_challenges', 
#     db.Model.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('challenge_id', Integer, ForeignKey('challenges.id'))
# )

# # جدول وسيط للعلاقة بين المستخدمين والمشاريع
# user_projects = Table(
#     'user_projects', 
#     db.Model.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('project_id', Integer, ForeignKey('projects.id'))
# )

# class User(db.Model):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     password_hash = Column(String(255), nullable=False)
#     profile_image = Column(String(255), default='default-avatar.png')
#     role = Column(String(20), default='user')
#     bio = Column(Text)
    
#     # المواهب
#     talents = relationship('UserTalent', back_populates='user')
#     primary_talent = Column(String(100))
    
#     # العلاقات
#     completed_challenges = relationship('Challenge', secondary=user_completed_challenges)
#     projects = relationship('Project', secondary=user_projects)
#     badges = relationship('UserBadge', back_populates='user')
    
#     # الروابط الاجتماعية
#     website = Column(String(255))
#     linkedin = Column(String(255))
#     github = Column(String(255))
#     twitter = Column(String(255))
#     facebook = Column(String(255))
#     instagram = Column(String(255))
#     behance = Column(String(255))
#     youtube = Column(String(255))
    
#     # معلومات أخرى
#     is_active = Column(Boolean, default=True)
#     last_login = Column(DateTime, default=datetime.utcnow)
#     reset_password_token = Column(String(255))
#     reset_password_expire = Column(DateTime)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')
    
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)
    
#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)
    
#     def __repr__(self):
#         return f'<User {self.name}>'

# class UserTalent(db.Model):
#     __tablename__ = 'user_talents'
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     talent_type = Column(String(100), nullable=False)
#     level = Column(String(20), default='مبتدئ')
#     score = Column(Float, default=0)
    
#     user = relationship('User', back_populates='talents')

# class UserBadge(db.Model):
#     __tablename__ = 'user_badges'
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     name = Column(String(100), nullable=False)
#     image = Column(String(255))
#     earned_at = Column(DateTime, default=datetime.utcnow)
#     description = Column(Text)
    
#     user = relationship('User', back_populates='badges')

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # العلاقات
    talents = db.relationship('UserTalent', backref='user', lazy='dynamic')
    projects = db.relationship('Project', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserTalent(db.Model):
    __tablename__ = 'user_talents'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    talent_id = db.Column(db.Integer, db.ForeignKey('talents.id'))
    skill_level = db.Column(db.Integer, default=1) 
    
    talent = db.relationship('Talent', backref='user_talents')