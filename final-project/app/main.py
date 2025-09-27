from fastapi import FastAPI
from .database import init_db
from .routers import students, courses, enrollments, admin

app = FastAPI(title="Student Management System API")
init_db()

app.include_router(admin.router)
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["Enrollments"])