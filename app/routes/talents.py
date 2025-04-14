from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.talent import Talent, UserTalent

talents_bp = Blueprint('talents', __name__)

@talents_bp.route('/', methods=['GET'])
def get_all_talents():
    talents = Talent.query.all()
    return jsonify([{
        'id': talent.id,
        'name': talent.name,
        'description': talent.description
    } for talent in talents]), 200

@talents_bp.route('/<int:talent_id>', methods=['GET'])
def get_talent(talent_id):
    talent = Talent.query.get_or_404(talent_id)
    return jsonify({
        'id': talent.id,
        'name': talent.name,
        'description': talent.description
    }), 200

@talents_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_talents():
    current_user_id = get_jwt_identity()
    user_talents = UserTalent.query.filter_by(user_id=current_user_id).all()
    
    result = []
    for user_talent in user_talents:
        talent = user_talent.talent
        result.append({
            'id': talent.id,
            'name': talent.name,
            'description': talent.description,
            'skill_level': user_talent.skill_level
        })
    
    return jsonify(result), 200

@talents_bp.route('/user/<int:talent_id>', methods=['POST'])
@jwt_required()
def add_user_talent(talent_id):
    current_user_id = get_jwt_identity()
    
    # التحقق من وجود الموهبة
    talent = Talent.query.get_or_404(talent_id)
    
    # التحقق من عدم وجود الموهبة لدى المستخدم مسبقًا
    existing = UserTalent.query.filter_by(user_id=current_user_id, talent_id=talent_id).first()
    if existing:
        return jsonify({'message': 'Talent already added for this user'}), 400
    
    # إضافة الموهبة للمستخدم
    user_talent = UserTalent(user_id=current_user_id, talent_id=talent_id)
    db.session.add(user_talent)
    db.session.commit()
    
    return jsonify({'message': 'Talent added successfully'}), 201