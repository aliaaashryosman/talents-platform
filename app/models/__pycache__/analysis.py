# models/analysis.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship

from . import db

class Analysis(db.Model):
    __tablename__ = 'analyses'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    talent_type = Column(String(100), nullable=False)
    overall_score = Column(Float, nullable=False)
    
    # العلاقات
    user = relationship('User', backref='analyses')
    project = relationship('Project', back_populates='analyses')
    criteria_scores = relationship('AnalysisCriteria', back_populates='analysis')
    strengths = relationship('AnalysisStrength', back_populates='analysis')
    weaknesses = relationship('AnalysisWeakness', back_populates='analysis')
    suggestions = relationship('AnalysisSuggestion', back_populates='analysis')
    
    # معلومات التحليل
    estimated_level = Column(String(20), nullable=False)
    compared_analysis_id = Column(Integer, ForeignKey('analyses.id'))
    compared_analysis = relationship('Analysis', remote_side=[id])
    improvement = Column(Float, default=0)
    ai_model_version = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Analysis {self.id} for Project {self.project_id}>'

class AnalysisCriteria(db.Model):
    __tablename__ = 'analysis_criteria'
    
    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    name = Column(String(100))
    score = Column(Float)
    description = Column(Text)
    
    analysis = relationship('Analysis', back_populates='criteria_scores')
    
    # بيانات المقارنة
    previous_score = Column(Float)
    improvement = Column(Float)

class AnalysisStrength(db.Model):
    __tablename__ = 'analysis_strengths'
    
    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    description = Column(Text)
    
    analysis = relationship('Analysis', back_populates='strengths')

class AnalysisWeakness(db.Model):
    __tablename__ = 'analysis_weaknesses'
    
    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    description = Column(Text)
    
    analysis = relationship('Analysis', back_populates='weaknesses')

class AnalysisSuggestion(db.Model):
    __tablename__ = 'analysis_suggestions'
    
    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    title = Column(String(255))
    description = Column(Text)
    priority = Column(String(20), default='متوسطة')
    
    # العلاقات
    resources = relationship('SuggestionResource', back_populates='suggestion')
    
    analysis = relationship('Analysis', back_populates='suggestions')

class SuggestionResource(db.Model):
    __tablename__ = 'suggestion_resources'
    
    id = Column(Integer, primary_key=True)
    suggestion_id = Column(Integer, ForeignKey('analysis_suggestions.id'))
    title = Column(String(255))
    type = Column(String(50))
    url = Column(String(500))
    
    suggestion = relationship('AnalysisSuggestion', back_populates='resources')