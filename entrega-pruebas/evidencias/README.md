# Evidencias de Pruebas

Esta carpeta debe contener las capturas de pantalla de Swagger UI para cada caso de prueba.

## Casos requeridos (según el enunciado)

### Cursos (P01-P05)
- `P01a-crear-curso.png` - POST /courses válido → 201
- `P01b-crear-curso-active-false.png` - POST /courses con active: false → 201
- `P01c-crear-curso-omitir-active.png` - POST /courses sin active → 201 (default true)
- `P01d-nombre-corto.png` - POST /courses nombre < 3 chars → 422
- `P01e-nombre-largo.png` - POST /courses nombre > 80 chars → 422
- `P01f-creditos-cero.png` - POST /courses credits: 0 → 422
- `P01g-creditos-siete.png` - POST /courses credits: 7 → 422
- `P01h-campos-faltantes.png` - POST /courses campos obligatorios ausentes → 422

- `P02a-listar-vacio.png` - GET /courses base vacía → 200 []
- `P02b-listar-con-datos.png` - GET /courses varios cursos → 200 [lista]

- `P03a-consultar-existente.png` - GET /courses/{id} existente → 200
- `P03b-consultar-inexistente.png` - GET /courses/999 → 404
- `P03c-consultar-id-invalido.png` - GET /courses/abc → 422

- `P04a-actualizar-valido.png` - PUT /courses/{id} datos válidos → 200
- `P04b-actualizar-active-false.png` - PUT /courses/{id} active: false → 200
- `P04c-actualizar-limites-validos.png` - PUT nombre 3/80 chars, credits 1/6 → 200
- `P04d-actualizar-limites-invalidos.png` - PUT nombre 2 chars → 422
- `P04e-actualizar-creditos-invalidos.png` - PUT credits 0/7 → 422
- `P04f-actualizar-campos-obligatorios.png` - PUT omitir active → 422
- `P04g-actualizar-inexistente.png` - PUT /courses/999 → 404
- `P04h-actualizar-id-invalido.png` - PUT /courses/abc → 422

- `P05a-eliminar-existente.png` - DELETE /courses/{id} → 200 {"message": "Course deleted"}
- `P05b-consultar-despues.png` - GET /courses/{id} eliminado → 404
- `P05c-lista-sin-eliminado.png` - GET /courses lista sin el eliminado → 200
- `P05d-otros-intactos.png` - Otros cursos permanecen → 200
- `P05e-eliminar-duplicado.png` - DELETE mismo ID → 404
- `P05f-eliminar-inexistente.png` - DELETE /courses/999 → 404
- `P05g-eliminar-id-invalido.png` - DELETE /courses/abc → 422

### Estudiantes (P06-P08)
- `P06a-crear-estudiante.png` - POST /students válido → 201
- `P06b-crear-omitir-active.png` - POST /students sin active → 201 (default true)
- `P06c-crear-active-false.png` - POST /students active: false → 201
- `P06d-nombre-corto.png` - POST nombre < 3 chars → 422
- `P06e-nombre-largo.png` - POST nombre > 80 chars → 422
- `P06f-semestre-cero.png` - POST semester: 0 → 422
- `P06g-semestre-once.png` - POST semester: 11 → 422
- `P06h-email-vacio.png` - POST email: "" → 422
- `P06i-campos-faltantes.png` - POST campos obligatorios ausentes → 422

- `P07a-listar-vacio.png` - GET /students base vacía → 200 []
- `P07b-listar-con-datos.png` - GET /students varios → 200 [lista]

- `P08a-consultar-existente.png` - GET /students/{id} existente → 200
- `P08b-consultar-inexistente.png` - GET /students/999 → 404
- `P08c-consultar-id-invalido.png` - GET /students/abc → 422

### Persistencia e Integración (P09)
- `P09a-reinicio-cursos.png` - Reiniciar Uvicorn, GET /courses → datos permanecen
- `P09b-reinicio-estudiantes.png` - Reiniciar Uvicorn, GET /students → datos permanecen
- `P09c-reinicio-put.png` - Reiniciar Uvicorn, cambios PUT permanecen → 200
- `P09d-reinicio-delete.png` - Reiniciar Uvicorn, cursos eliminados siguen eliminados → 404
- `P09e-integracion.png` - Operaciones de cursos no modifican estudiantes y viceversa

## Instrucciones

1. Ejecuta la API: `python -m uvicorn main:app --reload`
2. Abre http://127.0.0.1:8000/docs
3. Para cada caso: haz clic en "Try it out", ingresa datos, "Execute"
4. Captura la sección **Server response** (código HTTP + cuerpo JSON)
5. Guarda la imagen con el nombre indicado arriba en esta carpeta