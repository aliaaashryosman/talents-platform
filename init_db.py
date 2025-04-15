from app import create_app, db
from app.models.talent import Talent

def init_database():
    app = create_app()
    with app.app_context():
        # إنشاء قاعدة البيانات
        db.create_all()
        
        # التحقق من وجود المواهب مسبقًا
        if Talent.query.count() == 0:
            # إضافة المواهب
            talents = [
                Talent(name="تصميم الصور", description="تصميم الصور والرسومات والتعديل عليها"),
                Talent(name="البرمجة", description="كتابة التعليمات البرمجية وتطوير البرمجيات"),
                Talent(name="الصوت", description="تسجيل وتحرير الصوت والموسيقى"),
                Talent(name="الفيديو", description="إنتاج وتحرير مقاطع الفيديو"),
                Talent(name="تصميم واجهات التفاعل", description="تصميم واجهات المستخدم وتجربة المستخدم"),
                Talent(name="تحليل البيانات", description="جمع وتحليل وتفسير البيانات")
            ]
            
            # إضافة المواهب إلى قاعدة البيانات
            for talent in talents:
                db.session.add(talent)
            
            db.session.commit()
            print("تمت إضافة المواهب بنجاح!")
        else:
            print("المواهب موجودة بالفعل في قاعدة البيانات.")

if __name__ == "__main__":
    init_database()