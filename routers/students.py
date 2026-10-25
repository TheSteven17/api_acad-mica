from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database.database import get_session
from schemas.student import StudentCreate, StudentResponse
from services.student_service import create_student, get_students, get_student_by_id

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, session: Session = Depends(get_session)):
    return create_student(student, session)


@router.get("/", response_model=list[StudentResponse])
def read_students(session: Session = Depends(get_session)):
    return get_students(session)


@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, session: Session = Depends(get_session)):
    student = get_student_by_id(student_id, session)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student