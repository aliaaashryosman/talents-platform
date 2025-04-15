# models/review.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, Text, Float
from sqlalchemy.orm import relationship

from . import db

# جدول وسيط للعلاقة بين التقييمات والإعجابات
review_likes = Table(
    'review_likes', 
    db.Model.metadata,
    Column('review_id', Integer, ForeignKey('reviews.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Float, nullable=False)
    comment = Column(Text, nullable=False)
    
    # العلاقات
    project = relationship('Project', backref='reviews')
    user = relationship('User', backref='reviews')
    criteria = relationship('ReviewCriteria', back_populates='review')
    likes = relationship('User', secondary=review_likes)
    
    # معلومات التقييم
    is_edited = Column(Boolean, default=False)
    is_public = Column(Boolean, default=True)
    is_ai = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Review {self.id} for Project {self.project_id}>'
    
    # إضافة قيد فريد لمنع تكرار التقييمات
    __table_args__ = (
        db.UniqueConstraint('project_id', 'user_id', name='unique_user_project_review'),
    )

class ReviewCriteria(db.Model):
    __tablename__ = 'review_criteria'
    
    id = Column(Integer, primary_key=True)
    review_id = Column(Integer, ForeignKey('reviews.id'))
    name = Column(String(100))
    rating = Column(Float)
    
    review = relationship('Review', back_populates='criteria')