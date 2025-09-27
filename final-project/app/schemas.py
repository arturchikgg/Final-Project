from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    age: int
    enrollment_date: date

class StudentCreate(StudentBase): pass

class Student(StudentBase):
    id: int
    class Config: orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    credits: float

class CourseCreate(CourseBase): pass

class Course(CourseBase):
    id: int
    class Config: orm_mode = True

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int
    grade: Optional[str] = None

class EnrollmentCreate(EnrollmentBase): pass

class Enrollment(EnrollmentBase):
    id: int
    class Config: orm_mode = True

class StudentWithCourses(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    enrollment_date: date
    enrollments: List[Enrollment]
    class Config: orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class AdminLogin(BaseModel):
    username: str
    password: str