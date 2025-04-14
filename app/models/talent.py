from app import db

class Talent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Talent {self.name}>'

class UserTalent(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    talent_id = db.Column(db.Integer, db.ForeignKey('talent.id'), primary_key=True)
    skill_level = db.Column(db.Integer, default=1)  # مستوى المهارة من 1 إلى 10
    
    user = db.relationship('User', backref=db.backref('talents', lazy='dynamic'))
    talent = db.relationship('Talent', backref=db.backref('users', lazy='dynamic'))
    
    def __repr__(self):
        return f'<UserTalent {self.user_id}:{self.talent_id}>'