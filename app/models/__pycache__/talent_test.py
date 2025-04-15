# models/talent_test.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float, JSON
from sqlalchemy.orm import relationship

from . import db

class TalentTest(db.Model):
    __tablename__ = 'talent_tests'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    
    # العلاقات
    questions = relationship('TestQuestion', back_populates='test')
    
    # معلومات الاختبار
    duration = Column(Integer, default=15)  # بالدقائق
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<TalentTest {self.title}>'

class TestQuestion(db.Model):
    __tablename__ = 'test_questions'
    
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey('talent_tests.id'))
    text = Column(Text, nullable=False)
    type = Column(String(50), nullable=False)
    is_required = Column(Boolean, default=True)
    
    # العلاقات
    test = relationship('TalentTest', back_populates='questions')
    options = relationship('QuestionOption', back_populates='question')

class QuestionOption(db.Model):
    __tablename__ = 'question_options'
    
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('test_questions.id'))
    text = Column(String(255))
    image = Column(String(255))
    talent_type = Column(String(100))
    weight = Column(Float)
    
    question = relationship('TestQuestion', back_populates='options')