from app import create_app
from app.models import Challenge

app = create_app()

with app.app_context():
    # إضافة تحديات أولية
    challenges = [
        Challenge(title="تحدي التصميم", description="وصف التحدي الأول"),
        Challenge(title="تحدي البرمجة", description="وصف التحدي الثاني")
    ]
    
    for challenge in challenges:
        db.session.add(challenge) # type: ignore
    
    db.session.commit() # type: ignore
    print("تمت إضافة البيانات الأولية بنجاح!")