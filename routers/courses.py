from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database.database import get_session
from schemas.course import CourseCreate, CourseUpdate, CourseResponse
from services.course_service import create_course, list_courses, get_course, update_course, delete_course

router = APIRouter(prefix="/courses", tags=["Courses"])


# POST /courses: recibe datos validados y responde con el curso creado (201).
@router.post(
    "",
    response_model=CourseResponse,
    status_code=201
)
def create_course_endpoint(
    course: CourseCreate,
    session: Session = Depends(get_session)
):
    return create_course(course, session)


# GET /courses: devuelve todos los cursos como una lista.
@router.get(
    "",
    response_model=list[CourseResponse]
)
def list_courses_endpoint(
    session: Session = Depends(get_session)
):
    return list_courses(session)


# GET /courses/{course_id}: toma el ID de la URL y lo valida como entero.
@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def get_course_endpoint(
    course_id: int,
    session: Session = Depends(get_session)
):
    return get_course(course_id, session)


# PUT /courses/{course_id}: actualiza un curso existente.
@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
def modify_course(
    course_id: int,
    course_data: CourseUpdate,
    session: Session = Depends(get_session)
):
    updated_course = update_course(course_id, course_data, session)
    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course


# DELETE /courses/{course_id}: elimina un curso existente.
@router.delete(
    "/{course_id}",
    status_code=status.HTTP_200_OK
)
def delete_course_endpoint(
    course_id: int,
    session: Session = Depends(get_session)
):
    deleted = delete_course(course_id, session)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted"}