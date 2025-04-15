# models/test_result.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, JSON
from sqlalchemy.orm import relationship

from . import db

class TestResult(db.Model):
    __tablename__ = 'test_results'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    test_id = Column(Integer, ForeignKey('talent_tests.id'), nullable=False)
    
    # العلاقات
    user = relationship('User', backref='test_results')
    test = relationship('TalentTest', backref='results')
    answers = relationship('TestAnswer', back_populates='result')
    talent_scores = relationship('TalentScore', back_populates='result')
    recommendations = relationship('TalentRecommendation', back_populates='result')
    
    # النتائج
    primary_talent = Column(String(100))
    secondary_talent = Column(String(100))
    completed_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<TestResult {self.id} for User {self.user_id}>'

class TestAnswer(db.Model):
    __tablename__ = 'test_answers'
    
    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, ForeignKey('test_results.id'))
    question_id = Column(Integer, ForeignKey('test_questions.id'))
    answer_data = Column(JSON)  # لتخزين أنواع مختلفة من الإجابات
    
    result = relationship('TestResult', back_populates='answers')
    question = relationship('TestQuestion')

class TalentScore(db.Model):
    __tablename__ = 'talent_scores'
    
    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, ForeignKey('test_results.id'))
    talent = Column(String(100), nullable=False)
    score = Column(Float, nullable=False)
    level = Column(String(20), nullable=False)
    
    result = relationship('TestResult', back_populates='talent_scores')

class TalentRecommendation(db.Model):
    __tablename__ = 'talent_recommendations'
    
    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, ForeignKey('test_results.id'))
    talent = Column(String(100))
    description = Column(Text)
    suggested_level = Column(String(20))
    
    # العلاقات
    result = relationship('TestResult', back_populates='recommendations')
    next_steps = relationship('RecommendationStep', back_populates='recommendation')

class RecommendationStep(db.Model):
    __tablename__ = 'recommendation_steps'
    
    id = Column(Integer, primary_key=True)
    recommendation_id = Column(Integer, ForeignKey('talent_recommendations.id'))
    description = Column(Text)
    
    recommendation = relationship('TalentRecommendation', back_populates='next_steps')