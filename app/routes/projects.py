from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from app.models import Project, db
import os

projects_bp = Blueprint('projects', __name__, url_prefix='/api/projects')

UPLOAD_FOLDER = 'app/static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@projects_bp.route('/', methods=['POST'])
@jwt_required()
def upload_project():
    user_id = get_jwt_identity()
    file = request.files['file']
    talent_id = request.form['talent_id']
    
    filename = f"user_{user_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    
    project = Project(
        title=filename,
        file_path=file_path,
        user_id=user_id,
        talent_id=talent_id
    )
    db.session.add(project)
    db.session.commit()
    
    return jsonify({"message": "Project uploaded!", "id": project.id}), 201