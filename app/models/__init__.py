
# # models/__init__.py
# from flask_sqlalchemy import SQLAlchemy # type: ignore

# db = SQLAlchemy()

# # استيراد النماذج بعد تعريف كائن db
# from .user import User, UserTalent, UserBadge
# from .project import Project, ProjectFile
# from .challenge import Challenge, ChallengeCriteria, ChallengeResource # type: ignore
# from .review import Review, ReviewCriteria # type: ignore
# from .notification import Notification # type: ignore
# from .tool import Tool, ToolFeature # type: ignore
# from .analysis import Analysis, AnalysisCriteria, AnalysisStrength, AnalysisWeakness, AnalysisSuggestion, SuggestionResource
# from .talent_test import TalentTest, TestQuestion, QuestionOption # type: ignore
# from .test_result import TestResult, TestAnswer, TalentScore, TalentRecommendation, RecommendationStep # type: ignore

# from app.models.user import User
# from app.models.talent import Talent, UserTalent
# from app.models.project import Project
# from app.models.analysis import Analysis

from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

# استيراد جميع النماذج هنا
from .user import User, UserTalent
from .talent import Talent 
from .project import Project
from .analysis import Analysis, AnalysisStrength, AnalysisWeakness, AnalysisCriteria
from .challenge import Challenge # type: ignore

