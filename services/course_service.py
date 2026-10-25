# Los servicios realizan las operaciones de datos que solicitan los routers.
from fastapi import HTTPException
from sqlmodel import Session, select

from models.course import Course


def create_course(course_data, session: Session):
    # Convierte los datos de entrada en una entidad que puede persistirse.
    course = Course(
        name=course_data.name,
        credits=course_data.credits,
        active=course_data.active
    )

    # Registra el objeto en la sesión, todavía sin confirmar la transacción.
    session.add(course)
    # Confirma la inserción en la base de datos.
    session.commit()
    # Recarga los valores guardados, como el ID generado por SQLite.
    session.refresh(course)

    return course


def list_courses(session: Session):
    # Construye una consulta para recuperar todos los registros de Course.
    statement = select(Course)

    # Ejecuta la consulta y reúne los resultados en una lista.
    courses = session.exec(statement).all()

    return courses


def get_course(
    course_id: int,
    session: Session
):
    # Busca por clave primaria; devuelve None si no existe ese ID.
    course = session.get(
        Course,
        course_id
    )

    # Informa al cliente de un recurso inexistente con el estado HTTP 404.
    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


def update_course(
    course_id: int,
    course_data,
    session: Session
):
    # Busca el curso existente por su clave primaria.
    course = session.get(Course, course_id)

    # Si no existe, informa al cliente con 404.
    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    # Modifica los atributos del objeto existente.
    course.name = course_data.name
    course.credits = course_data.credits
    course.active = course_data.active

    # Confirma los cambios en la base de datos.
    session.commit()
    # Recarga el registro para asegurar los valores guardados.
    session.refresh(course)

    return course


def delete_course(course_id: int, session: Session) -> bool:
    course = session.get(Course, course_id)
    if not course:
        return False
    session.delete(course)
    session.commit()
    return True