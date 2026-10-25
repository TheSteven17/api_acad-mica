from pydantic import BaseModel, Field


# Esquema de entrada: valida el cuerpo JSON antes de ejecutar el endpoint.
class StudentCreate(BaseModel):
    # El nombre debe tener entre 3 y 80 caracteres.
    name: str = Field(min_length=3, max_length=80)
    # El email no puede estar vacío.
    email: str = Field(min_length=1)
    # Solo se admiten estudiantes con semestre entre 1 y 10.
    semester: int = Field(ge=1, le=10)
    # Un estudiante nuevo queda activo si no se indica otro valor.
    active: bool = True


# Esquema de salida: define los campos devueltos al cliente, incluido el ID.
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    semester: int
    active: bool