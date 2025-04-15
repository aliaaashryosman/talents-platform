# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from app import db
# from app.models.user import User

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
    
#     # التحقق من وجود البيانات المطلوبة
#     if not data or not data.get('username') or not data.get('email') or not data.get('password'):
#         return jsonify({'message': 'Missing required fields'}), 400
    
#     # التحقق من عدم وجود المستخدم مسبقًا
#     if User.query.filter_by(username=data['username']).first():
#         return jsonify({'message': 'Username already exists'}), 400
    
#     if User.query.filter_by(email=data['email']).first():
#         return jsonify({'message': 'Email already exists'}), 400
    
#     # إنشاء مستخدم جديد
#     user = User(username=data['username'], email=data['email'])
#     user.set_password(data['password'])
    
#     db.session.add(user)
#     db.session.commit()
    
#     return jsonify({'message': 'User registered successfully'}), 201

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
    
#     # التحقق من وجود البيانات المطلوبة
#     if not data or not data.get('username') or not data.get('password'):
#         return jsonify({'message': 'Missing username or password'}), 400
    
#     # البحث عن المستخدم
#     user = User.query.filter_by(username=data['username']).first()
    
#     # التحقق من وجود المستخدم وصحة كلمة المرور
#     if not user or not user.check_password(data['password']):
#         return jsonify({'message': 'Invalid username or password'}), 401
    
#     # إنشاء توكن الوصول
#     access_token = create_access_token(identity=user.id)
    
#     return jsonify({'access_token': access_token, 'user_id': user.id, 'username': user.username}), 200

# @auth_bp.route('/profile', methods=['GET'])
# @jwt_required()
# def profile():
#     current_user_id = get_jwt_identity()
#     user = User.query.get(current_user_id)
    
#     if not user:
#         return jsonify({'message': 'User not found'}), 404
    
#     return jsonify({
#         'id': user.id,
#         'username': user.username,
#         'email': user.email,
#         'created_at': user.created_at.isoformat()
#     }), 200


from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity # type: ignore
from app.models import User, db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(
        username=data['username'],
        email=data['email'],
        password=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered!"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401