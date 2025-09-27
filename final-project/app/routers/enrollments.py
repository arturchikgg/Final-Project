from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, auth

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Enrollment)
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    # Проверяем существование студента и курса
    student = crud.get_student(db, enrollment.student_id)
    course = crud.get_course(db, enrollment.course_id)
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    return crud.enroll_student(db, enrollment)

@router.get("/", response_model=list[schemas.Enrollment])
def list_enrollments(db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    return crud.get_enrollments(db)

@router.put("/{enrollment_id}/grade", response_model=schemas.Enrollment)
def assign_grade(enrollment_id: int, grade: str, db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    enrollment = crud.get_enrollment(db, enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return crud.assign_grade(db, enrollment_id, grade)