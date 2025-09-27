from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import schemas, crud, database, auth

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    return crud.create_student(db, student)

@router.get("/", response_model=list[schemas.Student])
def list_students(
    db: Session = Depends(get_db),
    name: str = Query(None),
    email: str = Query(None),
    user=Depends(auth.verify_jwt)
):
    if name or email:
        return crud.search_students(db, name=name, email=email)
    return crud.get_students(db)

@router.get("/{student_id}", response_model=schemas.StudentWithCourses)
def get_student_with_courses(student_id: int, db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    student = crud.get_student_with_courses(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    db_student = crud.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.update_student(db, student_id, student)

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db), user=Depends(auth.verify_jwt)):
    db_student = crud.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.delete_student(db, student_id)
    return {"ok": True}