# Documentación de la API - Tribu Backend

## URL Base

- **Desarrollo**: `http://localhost:8000/api`
- **Producción**: `https://tribu-backend.onrender.com/api`

## Autenticación

La API utiliza autenticación basada en sesiones de Django. Para endpoints protegidos, se requiere estar autenticado.

## Endpoints

### 1. Servicios

#### Listar todos los servicios
```http
GET /api/services/
```

**Respuesta exitosa (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Corte de Cabello",
    "description": "Corte profesional con asesoría de imagen",
    "duration": 30,
    "price": "15000.00",
    "image_url": "https://...",
    "is_active": true,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Crear un servicio
```http
POST /api/services/
Content-Type: application/json

{
  "name": "Corte de Cabello",
  "description": "Descripción del servicio",
  "duration": 30,
  "price": "15000.00",
  "image_url": "https://...",
  "is_active": true
}
```

#### Actualizar un servicio
```http
PATCH /api/services/{id}/
Content-Type: application/json

{
  "price": "18000.00"
}
```

#### Eliminar un servicio
```http
DELETE /api/services/{id}/
```

---

### 2. Profesionales

#### Listar todos los profesionales
```http
GET /api/professionals/
```

**Respuesta exitosa (200 OK):**
```json
[
  {
    "id": 1,
    "name": "María González",
    "bio": "Estilista profesional con 10 años de experiencia",
    "photo_url": "https://...",
    "specialties": "Corte, Color, Peinados",
    "specialties_list": ["Corte", "Color", "Peinados"],
    "is_active": true,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Obtener fechas disponibles de un profesional
```http
GET /api/professionals/{id}/available_dates/?days=30
```

**Parámetros de consulta:**
- `days` (opcional): Número de días a futuro (por defecto: 30)

**Respuesta:**
```json
{
  "dates": [
    "2024-01-15",
    "2024-01-16",
    "2024-01-17"
  ]
}
```

---

### 3. Horarios

#### Listar horarios
```http
GET /api/schedules/?professional_id=1&date=2024-01-15&is_available=true
```

**Parámetros de consulta:**
- `professional_id` (opcional): ID del profesional
- `date` (opcional): Fecha en formato YYYY-MM-DD
- `is_available` (opcional): true/false

**Respuesta:**
```json
[
  {
    "id": 1,
    "professional": 1,
    "professional_name": "María González",
    "date": "2024-01-15",
    "time": "10:00:00",
    "is_available": true,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Crear horarios en lote
```http
POST /api/schedules/bulk_create/
Content-Type: application/json

{
  "schedules": [
    {
      "professional": 1,
      "date": "2024-01-15",
      "time": "10:00:00",
      "is_available": true
    },
    {
      "professional": 1,
      "date": "2024-01-15",
      "time": "11:00:00",
      "is_available": true
    }
  ]
}
```

---

### 4. Reservas

#### Listar reservas
```http
GET /api/bookings/?professional_id=1&status=pending&date=2024-01-15
```

**Parámetros de consulta:**
- `professional_id` (opcional): ID del profesional
- `status` (opcional): pending, confirmed, cancelled, completed
- `date` (opcional): Fecha en formato YYYY-MM-DD
- `user_id` (opcional): ID del usuario

**Respuesta:**
```json
[
  {
    "id": 1,
    "professional": 1,
    "professional_name": "María González",
    "service": 1,
    "service_name": "Corte de Cabello",
    "service_duration": 30,
    "service_price": "15000.00",
    "client_name": "Juan Pérez",
    "client_email": "juan@example.com",
    "client_phone": "+56912345678",
    "date": "2024-01-15",
    "time": "10:00:00",
    "status": "pending",
    "notes": "Preferencia por corte degradado",
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Crear reserva
```http
POST /api/bookings/
Content-Type: application/json

{
  "professional": 1,
  "service": 1,
  "client_name": "Juan Pérez",
  "client_email": "juan@example.com",
  "client_phone": "+56912345678",
  "date": "2024-01-15",
  "time": "10:00:00",
  "notes": "Notas adicionales"
}
```

**Validaciones:**
- El horario debe estar disponible
- No puede haber otra reserva activa en el mismo horario

#### Cancelar reserva
```http
POST /api/bookings/{id}/cancel/
```

**Respuesta:**
```json
{
  "status": "Reserva cancelada exitosamente"
}
```

#### Confirmar reserva
```http
POST /api/bookings/{id}/confirm/
```

#### Completar reserva
```http
POST /api/bookings/{id}/complete/
```

---

### 5. Testimonios

#### Listar testimonios aprobados
```http
GET /api/testimonials/?service_id=1
```

**Parámetros de consulta:**
- `service_id` (opcional): Filtrar por servicio

**Respuesta:**
```json
[
  {
    "id": 1,
    "author": "María Rodríguez",
    "content": "Excelente servicio, muy profesionales",
    "rating": 5,
    "service": 1,
    "service_name": "Corte de Cabello",
    "is_approved": true,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Crear testimonio
```http
POST /api/testimonials/
Content-Type: application/json

{
  "author": "Juan Pérez",
  "content": "Excelente atención",
  "rating": 5,
  "service": 1
}
```

**Nota:** Los testimonios nuevos requieren aprobación de un administrador.

#### Aprobar testimonio (Admin)
```http
POST /api/testimonials/{id}/approve/
```

---

### 6. Galería

#### Listar imágenes
```http
GET /api/gallery/?category=cortes
```

**Parámetros de consulta:**
- `category` (opcional): Filtrar por categoría

**Respuesta:**
```json
[
  {
    "id": 1,
    "title": "Corte Degradado",
    "description": "Estilo moderno",
    "image_url": "https://...",
    "category": "cortes",
    "is_active": true,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
]
```

#### Subir imagen
```http
POST /api/gallery/
Content-Type: multipart/form-data

title=Corte Degradado
description=Estilo moderno
category=cortes
image=<archivo>
```

---

## Códigos de Estado HTTP

- `200 OK`: Solicitud exitosa
- `201 Created`: Recurso creado exitosamente
- `204 No Content`: Solicitud exitosa sin contenido
- `400 Bad Request`: Error en los datos enviados
- `401 Unauthorized`: No autenticado
- `403 Forbidden`: Sin permisos
- `404 Not Found`: Recurso no encontrado
- `500 Internal Server Error`: Error del servidor

## Manejo de Errores

Todos los errores devuelven un formato JSON:

```json
{
  "error": "Mensaje de error descriptivo"
}
```

O con detalles:

```json
{
  "field_name": ["Error específico del campo"]
}
```

## Paginación

Los endpoints que retornan listas están paginados:

```json
{
  "count": 100,
  "next": "http://api/endpoint/?page=2",
  "previous": null,
  "results": [...]
}
```

## Rate Limiting

En producción, la API está limitada a:
- 100 requests por minuto por IP
- 1000 requests por hora por IP

## CORS

El backend acepta requests desde:
- Frontend de desarrollo: `http://localhost:5173`
- Frontend de producción: `https://tribu-theta.vercel.app`

## Seguridad

- Todas las conexiones en producción deben usar HTTPS
- Los datos sensibles deben enviarse en el body, no en la URL
- Implementar rate limiting en el cliente
- Validar siempre los datos en el backend

