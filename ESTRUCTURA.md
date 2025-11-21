# 📁 Estructura del Backend - Arquitectura Modular

El backend de Tribu está organizado siguiendo las mejores prácticas de Django, con una arquitectura modular donde cada funcionalidad está en su propia app independiente.

## 🏗️ Apps del Proyecto

### 1. **accounts** - Gestión de Usuarios
```
accounts/
├── models.py          # UserProfile (extensión de User)
├── serializers.py     # UserSerializer, UserProfileSerializer
├── views.py           # UserViewSet con endpoint /me
├── admin.py           # Admin de perfiles
└── urls.py            # /api/accounts/
```

**Funcionalidades:**
- Perfil extendido de usuario con rol y teléfono
- Endpoint `/api/accounts/users/me/` para obtener usuario actual
- Roles: admin, worker, client

---

### 2. **services** - Servicios
```
services/
├── models.py          # Service (nombre, descripción, precio, duración)
├── serializers.py     # ServiceSerializer
├── views.py           # ServiceViewSet con búsqueda y filtros
├── admin.py           # Admin de servicios
└── urls.py            # /api/services/
```

**Funcionalidades:**
- CRUD completo de servicios
- Búsqueda por nombre y descripción
- Ordenamiento por precio y duración
- Servicios activos/inactivos

---

### 3. **professionals** - Profesionales
```
professionals/
├── models.py          # Professional (nombre, bio, especialidades)
├── serializers.py     # ProfessionalSerializer con especialties_list
├── views.py           # ProfessionalViewSet + available_dates action
├── admin.py           # Admin de profesionales
└── urls.py            # /api/professionals/
```

**Funcionalidades:**
- CRUD completo de profesionales
- Endpoint `/api/professionals/{id}/available_dates/` para fechas disponibles
- Búsqueda por nombre, bio y especialidades
- Profesionales activos/inactivos

---

### 4. **schedules** - Horarios
```
schedules/
├── models.py          # Schedule (profesional, fecha, hora, disponibilidad)
├── serializers.py     # ScheduleSerializer
├── views.py           # ScheduleViewSet + bulk_create action
├── admin.py           # Admin de horarios
└── urls.py            # /api/schedules/
```

**Funcionalidades:**
- CRUD de horarios individuales
- Endpoint `/api/schedules/bulk_create/` para crear múltiples horarios
- Filtros por profesional, fecha y disponibilidad
- Unique constraint: un horario por profesional/fecha/hora

---

### 5. **bookings** - Reservas
```
bookings/
├── models.py          # Booking (profesional, servicio, cliente, fecha/hora, estado)
├── serializers.py     # BookingSerializer con validación de disponibilidad
├── views.py           # BookingViewSet + cancel/confirm/complete actions
├── admin.py           # Admin de reservas
└── urls.py            # /api/bookings/
```

**Funcionalidades:**
- CRUD completo de reservas
- Validación automática de disponibilidad
- Estados: pending, confirmed, cancelled, completed
- Endpoints adicionales:
  - `/api/bookings/{id}/cancel/` - Cancela y libera horario
  - `/api/bookings/{id}/confirm/` - Confirma reserva
  - `/api/bookings/{id}/complete/` - Marca como completada
- Filtros por profesional, fecha, estado, usuario

---

### 6. **testimonials** - Testimonios
```
testimonials/
├── models.py          # Testimonial (autor, contenido, rating, servicio)
├── serializers.py     # TestimonialSerializer
├── views.py           # TestimonialViewSet + approve action
├── admin.py           # Admin con acción de aprobación en lote
└── urls.py            # /api/testimonials/
```

**Funcionalidades:**
- CRUD de testimonios
- Sistema de aprobación (solo aprobados son públicos)
- Rating de 1 a 5 estrellas
- Endpoint `/api/testimonials/{id}/approve/` para aprobar
- Filtro por servicio

---

### 7. **gallery** - Galería de Imágenes
```
gallery/
├── models.py          # GalleryImage (título, imagen, categoría)
├── serializers.py     # GalleryImageSerializer
├── views.py           # GalleryImageViewSet
├── admin.py           # Admin de galería
└── urls.py            # /api/gallery/
```

**Funcionalidades:**
- CRUD de imágenes
- Upload de archivos (multipart/form-data)
- Categorización de imágenes
- Filtro por categoría
- Imágenes activas/inactivas

---

## 📊 Relaciones entre Modelos

```
User (Django) ←─┐
                │
UserProfile ────┘

Professional ──┬── Schedule
               │
               └── Booking ──┬── Service
                             │
                             └── User (opcional)

Service ──┬── Booking
          │
          └── Testimonial
```

---

## 🔄 Flujo de una Reserva

1. **Cliente selecciona servicio y profesional**
   - GET `/api/services/`
   - GET `/api/professionals/`

2. **Verifica fechas disponibles**
   - GET `/api/professionals/{id}/available_dates/`

3. **Selecciona fecha y obtiene horas disponibles**
   - GET `/api/schedules/?professional_id=X&date=YYYY-MM-DD&is_available=true`

4. **Crea la reserva**
   - POST `/api/bookings/`
   - Validación automática de disponibilidad
   - Horario se marca como no disponible

5. **Gestión de la reserva**
   - POST `/api/bookings/{id}/confirm/` - Administrador confirma
   - POST `/api/bookings/{id}/complete/` - Marca como completada
   - POST `/api/bookings/{id}/cancel/` - Cancela y libera horario

---

## 🛠️ Ventajas de esta Arquitectura

### ✅ Modularidad
- Cada app es independiente y reutilizable
- Fácil de mantener y extender
- Código organizado por funcionalidad

### ✅ Escalabilidad
- Agregar nuevas funcionalidades = crear nueva app
- Las apps pueden moverse a microservicios fácilmente
- Tests independientes por app

### ✅ Claridad
- Estructura clara y predecible
- Fácil de navegar para nuevos desarrolladores
- Separación de responsabilidades

### ✅ Best Practices
- Sigue convenciones de Django
- Código limpio y profesional
- Fácil de documentar y mantener

---

## 📝 Convenciones de Código

### Modelos
- Nombres en singular (Service, Booking, etc.)
- `verbose_name` en español para el admin
- `__str__()` descriptivo
- Meta con ordering apropiado

### Serializers
- Nombre del modelo + Serializer
- `read_only_fields` para timestamps
- Validaciones en `validate()`
- Campos calculados con `SerializerMethodField`

### Views
- ViewSets para operaciones CRUD
- Actions para operaciones custom (`@action`)
- Permisos apropiados
- Filters y ordering configurados

### URLs
- Router de DRF para ViewSets
- Rutas RESTful estándar
- Prefijo `/api/` en URLs principales

---

## 🚀 Comandos Útiles

### Crear migraciones por app
```bash
python manage.py makemigrations accounts
python manage.py makemigrations services
# etc...
```

### Migrar
```bash
python manage.py migrate
```

### Ver estructura de la base de datos
```bash
python manage.py dbshell
```

### Pruebas por app
```bash
python manage.py test accounts
python manage.py test services
# etc...
```

---

## 📦 Dependencias entre Apps

- **schedules** depende de **professionals**
- **bookings** depende de **professionals** y **services**
- **testimonials** depende de **services**
- **accounts** es independiente (extiende User de Django)
- **gallery** es independiente

**Nota:** Las dependencias circulares se evitan con imports locales cuando es necesario.

---

## 🔐 Permisos y Seguridad

- Todos los endpoints permiten acceso público (AllowAny) por defecto
- Los testimonios sin aprobar solo son visibles para staff
- Se puede extender con permisos más granulares por app
- Preparado para agregar autenticación JWT/Token

---

Esta estructura facilita el mantenimiento, testing y escalabilidad del proyecto. Cada app es un módulo autocontenido que puede ser desarrollado, testeado y desplegado independientemente.

