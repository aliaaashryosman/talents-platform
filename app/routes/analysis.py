from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from app.models import Project, Analysis, db
from app.services.ai_service import analyze_image

analysis_bp = Blueprint('analysis', __name__, url_prefix='/api/analyze')

@analysis_bp.route('/<int:project_id>', methods=['POST'])
@jwt_required()
def analyze(project_id):
    project = Project.query.get_or_404(project_id)
    result = analyze_image(project.file_path)
    
    analysis = Analysis(
        project_id=project.id,
        strengths=result['strengths'],
        weaknesses=result['weaknesses'],
        score=result['score']
    )
    db.session.add(analysis)
    db.session.commit()
    
    return jsonify(result)