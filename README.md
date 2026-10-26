# API Académica

API educativa para crear y consultar cursos y estudiantes académicos con **FastAPI, SQLModel y SQLite**. El código implementa una arquitectura desacoplada (Routers → Servicios → Modelos) para facilitar el mantenimiento y la escalabilidad.

La explicación detallada del proyecto, la práctica con Swagger y los ejercicios están en la [guía para estudiantes](docs.md).

## Funcionalidades

### 📚 Cursos (Courses)
- Crear cursos con nombre, créditos y estado activo.
- Consultar todos los cursos o buscar uno por su identificador.
- Validar los datos de entrada y responder con errores HTTP.

### 🎓 Estudiantes (Students)
- Registro de estudiantes con validación de datos.
- Consulta de lista completa de estudiantes.
- Consulta de estudiantes individuales por ID.

### 💾 Persistencia
- Todos los datos se conservan en una base de datos SQLite local (`database.db`), asegurando que la información no se pierda al reiniciar el servidor.

## Tecnologías

| Herramienta | Uso |
| --- | --- |
| FastAPI | Aplicación web, rutas y documentación interactiva. |
| Uvicorn | Servidor que ejecuta la API. |
| SQLModel | Modelos de tablas y operaciones de base de datos. |
| Pydantic | Esquemas y validación de datos. |
| SQLite | Almacenamiento en el archivo `database.db`. |

Las versiones utilizadas están en [requirements.txt](requirements.txt). El proyecto se ha ejecutado con **Python 3.12**.

## Inicio rápido

Abre una terminal en la carpeta del proyecto, donde está `main.py`.

### 1. Crear y activar el entorno virtual

En Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalar las dependencias
```bash
python -m pip install -r requirements.txt
```

### 3. Ejecutar la API
```bash
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Abre la [documentación interactiva Swagger](http://127.0.0.1:8000/docs) para probar los endpoints con **Try it out → Execute**.

## Endpoints

### Cursos (CRUD completo)
| Método | Ruta | Operación | Estado éxito |
| --- | --- | --- | --- |
| `POST` | `/courses` | Crear un curso. | `201` |
| `GET` | `/courses` | Listar todos los cursos. | `200` |
| `GET` | `/courses/{id}` | Consultar curso por ID. | `200` |
| `PUT` | `/courses/{id}` | Actualizar curso completo. | `200` |
| `DELETE` | `/courses/{id}` | Eliminar curso. | `200` |

### Estudiantes (CREATE + READ)
| Método | Ruta | Operación | Estado éxito |
| --- | --- | --- | --- |
| `POST` | `/students` | Registrar estudiante. | `201` |
| `GET` | `/students` | Listar estudiantes. | `200` |
| `GET` | `/students/{id}` | Consultar estudiante por ID. | `200` |

### Códigos de error
| Código | Significado |
| --- | --- |
| `404` | Recurso no encontrado (ID inexistente) |
| `422` | Error de validación (datos inválidos o ID no entero) |

## Estructura del proyecto

```text
api_acad-mica/
├── main.py                     # Aplicación y ciclo de vida
├── database/
│   └── database.py             # Motor SQLite y sesiones
├── models/
│   ├── course.py               # Modelo de la tabla de cursos
│   └── student.py              # Modelo de la tabla de estudiantes
├── schemas/
│   ├── course.py               # Esquemas de entrada y salida de cursos
│   └── student.py              # Esquemas de entrada y salida de estudiantes
├── routers/
│   ├── courses.py              # Endpoints HTTP de cursos
│   └── students.py             # Endpoints HTTP de estudiantes
├── services/
│   ├── course_service.py        # Lógica de negocio de cursos
│   └── student_service.py      # Lógica de negocio de estudiantes
├── requirements.txt             # Dependencias
├── docs.md                     # Guía didáctica detallada
└── README.md                    # Presentación e inicio rápido
```

El flujo principal es: **petición HTTP → router y validación → servicio → base de datos → respuesta JSON**.
