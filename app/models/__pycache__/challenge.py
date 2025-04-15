# # models/challenge.py
# from datetime import datetime
# from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Text
# from sqlalchemy.orm import relationship

# from . import db

# # جدول وسيط للعلاقة بين التحديات والمشاركين
# challenge_participants = Table(
#     'challenge_participants', 
#     db.Model.metadata,
#     Column('challenge_id', Integer, ForeignKey('challenges.id')),
#     Column('user_id', Integer, ForeignKey('users.id'))
# )

# # جدول وسيط للعلاقة بين التحديات والأدوات الموصى بها
# challenge_tools = Table(
#     'challenge_tools', 
#     db.Model.metadata,
#     Column('challenge_id', Integer, ForeignKey('challenges.id')),
#     Column('tool_id', Integer, ForeignKey('tools.id'))
# )

# class Challenge(db.Model):
#     __tablename__ = 'challenges'
    
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), nullable=False)
#     description = Column(Text, nullable=False)
#     talent_type = Column(String(100), nullable=False)
#     difficulty_level = Column(String(20), default='متوسط')
#     image = Column(String(255))
    
#     # العلاقات
#     criteria = relationship('ChallengeCriteria', back_populates='challenge')
#     resources = relationship('ChallengeResource', back_populates='challenge')
#     participants = relationship('User', secondary=challenge_participants)
#     submissions = relationship('Project', backref='from_challenge')
#     recommended_tools = relationship('Tool', secondary=challenge_tools)
    
#     # معلومات التحدي
#     start_date = Column(DateTime, default=datetime.utcnow)
#     end_date = Column(DateTime, nullable=False)
#     is_active = Column(Boolean, default=True)
#     created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
#     creator = relationship('User')
#     is_featured = Column(Boolean, default=False)
    
#     # المكافآت
#     badge_name = Column(String(100))
#     badge_image = Column(String(255))
#     badge_description = Column(Text)
#     skill_points = Column(Integer, default=0)
#     certificate_template = Column(String(255))
    
#     # التسلسل
#     is_sequential = Column(Boolean, default=False)
#     sequence_number = Column(Integer, default=1)
#     previous_challenge_id = Column(Integer, ForeignKey('challenges.id'))
#     previous_challenge = relationship('Challenge', remote_side=[id], backref='next_challenge', uselist=False)
    
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     def __repr__(self):
#         return f'<Challenge {self.title}>'

# class ChallengeCriteria(db.Model):
#     __tablename__ = 'challenge_criteria'
    
#     id = Column(Integer, primary_key=True)
#     challenge_id = Column(Integer, ForeignKey('challenges.id'))
#     name = Column(String(100), nullable=False)
#     description = Column(Text)
#     weight = Column(Integer, default=5)
    
#     challenge = relationship('Challenge', back_populates='criteria')

# class ChallengeResource(db.Model):
#     __tablename__ = 'challenge_resources'
    
#     id = Column(Integer, primary_key=True)
#     challenge_id = Column(Integer, ForeignKey('challenges.id'))
#     title = Column(String(255), nullable=False)
#     description = Column(Text)
#     type = Column(String(50))
#     url = Column(String(500))
    
#     challenge = relationship('Challenge', back_populates='resources')


from datetime import datetime
from . import db

class Challenge(db.Model):
    __tablename__ = 'challenges'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    talent_id = db.Column(db.Integer, db.ForeignKey('talents.id'))
    talent = db.relationship('Talent', backref='challenges')
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Challenge {self.title}>'