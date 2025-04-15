# models/tool.py
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship

from . import db

class Tool(db.Model):
    __tablename__ = 'tools'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(255))
    url = Column(String(500))
    is_external = Column(Boolean, default=False)
    
    # العلاقات
    features = relationship('ToolFeature', back_populates='tool')
    
    # معلومات أخرى
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Tool {self.name}>'

class ToolFeature(db.Model):
    __tablename__ = 'tool_features'
    
    id = Column(Integer, primary_key=True)
    tool_id = Column(Integer, ForeignKey('tools.id'))
    name = Column(String(255))
    description = Column(Text)
    
    tool = relationship('Tool', back_populates='features')