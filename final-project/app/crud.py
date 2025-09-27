from sqlalchemy.orm import Session

from . import models
from . import schemas

# Students
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip=0, limit=100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = get_student(db, student_id)
    for var, value in vars(student).items():
        setattr(db_student, var, value) if value else None
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    db.delete(db_student)
    db.commit()
    return db_student

def search_students(db: Session, name=None, email=None):
    query = db.query(models.Student)
    if name:
        query = query.filter(models.Student.name.ilike(f"%{name}%"))
    if email:
        query = query.filter(models.Student.email.ilike(f"%{email}%"))
    return query.all()

def get_student_with_courses(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

# Courses
def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session):
    return db.query(models.Course).all()

def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = get_course(db, course_id)
    for var, value in vars(course).items():
        setattr(db_course, var, value) if value else None
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    db.delete(db_course)
    db.commit()
    return db_course

# Enrollments
def enroll_student(db: Session, enrollment: schemas.EnrollmentCreate):
    db_enrollment = models.Enrollment(**enrollment.dict())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def assign_grade(db: Session, enrollment_id: int, grade: str):
    enrollment = db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()
    enrollment.grade = grade
    db.commit()
    db.refresh(enrollment)
    return enrollment

def get_enrollments(db: Session):
    return db.query(models.Enrollment).all()

def get_enrollment(db: Session, enrollment_id: int):
    return db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()