# models/notification.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from . import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = Column(Integer, primary_key=True)
    recipient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    link = Column(String(500))
    icon = Column(String(255))
    is_read = Column(Boolean, default=False)
    priority = Column(String(20), default='متوسط')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # العلاقات
    recipient = relationship('User', foreign_keys=[recipient_id], backref='received_notifications')
    sender = relationship('User', foreign_keys=[sender_id], backref='sent_notifications')
    
    def __repr__(self):
        return f'<Notification {self.id} for User {self.recipient_id}>'