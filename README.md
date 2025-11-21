# Tribu Backend API - Django REST Framework

Backend API modular para el sistema de gestión de La Tribu - Salón y Barbería.

## 🏗️ Arquitectura Modular

Este proyecto sigue las mejores prácticas de Django con una arquitectura modular:

```
backend/
├── accounts/          # Gestión de usuarios y perfiles
├── services/          # Servicios ofrecidos
├── professionals/     # Profesionales y sus horarios
├── schedules/         # Horarios disponibles
├── bookings/          # Sistema de reservas
├── testimonials/      # Testimonios de clientes
└── gallery/           # Galería de imágenes
```

Cada app es independiente, escalable y fácil de mantener. Ver [ESTRUCTURA.md](ESTRUCTURA.md) para detalles completos.

## 🚀 Inicio Rápido

### Requisitos
- Python 3.11+
- PostgreSQL (producción) o SQLite (desarrollo)

### Instalación

1. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno:**
Crear archivo `.env` (ver `.env.example`)

4. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

5. **Crear superusuario:**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor:**
```bash
python manage.py runserver
```

API disponible en: `http://localhost:8000/api/`
Admin panel: `http://localhost:8000/admin/`

## 📡 API Endpoints

### Cuentas
- `GET /api/accounts/users/` - Listar usuarios
- `GET /api/accounts/users/me/` - Usuario actual

### Servicios
- `GET /api/services/` - Listar servicios
- `POST /api/services/` - Crear servicio
- `GET /api/services/{id}/` - Detalle
- `PATCH /api/services/{id}/` - Actualizar
- `DELETE /api/services/{id}/` - Eliminar

### Profesionales
- `GET /api/professionals/` - Listar profesionales
- `GET /api/professionals/{id}/available_dates/` - Fechas disponibles

### Horarios
- `GET /api/schedules/` - Listar horarios (con filtros)
- `POST /api/schedules/bulk_create/` - Crear múltiples horarios

### Reservas
- `GET /api/bookings/` - Listar reservas (con filtros)
- `POST /api/bookings/` - Crear reserva
- `POST /api/bookings/{id}/cancel/` - Cancelar
- `POST /api/bookings/{id}/confirm/` - Confirmar
- `POST /api/bookings/{id}/complete/` - Completar

### Testimonios
- `GET /api/testimonials/` - Listar testimonios aprobados
- `POST /api/testimonials/` - Crear testimonio
- `POST /api/testimonials/{id}/approve/` - Aprobar

### Galería
- `GET /api/gallery/` - Listar imágenes
- `POST /api/gallery/` - Subir imagen

Ver [API_DOCS.md](API_DOCS.md) para documentación completa.

## 🗄️ Modelos

### UserProfile (accounts)
Perfil extendido de usuario con rol (admin/worker/client)

### Service (services)
Servicios ofrecidos: nombre, descripción, precio, duración

### Professional (professionals)
Profesionales que ofrecen servicios con especialidades

### Schedule (schedules)
Horarios disponibles por profesional y fecha

### Booking (bookings)
Reservas con validación automática de disponibilidad

### Testimonial (testimonials)
Testimonios con sistema de aprobación

### GalleryImage (gallery)
Imágenes categorizadas de trabajos realizados

## 🛠️ Características Técnicas

- ✅ Django 5.0 + Django REST Framework
- ✅ PostgreSQL en producción
- ✅ CORS configurado
- ✅ Validaciones robustas
- ✅ Admin panel personalizado
- ✅ Arquitectura modular
- ✅ Código limpio y escalable
- ✅ Documentado completamente

## 📦 Deployment

### Render

Ver [DEPLOYMENT.md](DEPLOYMENT.md) para guía completa.

**Pasos rápidos:**
1. Crear PostgreSQL en Render
2. Crear Web Service conectado a GitHub
3. Configurar variables de entorno
4. Deploy automático

URL de producción: `https://tribu-backend.onrender.com`

## 🧪 Testing

```bash
# Todos los tests
python manage.py test

# Por app
python manage.py test accounts
python manage.py test bookings
```

## 📝 Desarrollo

### Agregar nueva funcionalidad

1. Crear nueva app:
```bash
python manage.py startapp mi_app
```

2. Agregar a `INSTALLED_APPS` en settings.py

3. Crear modelos, serializers, views, urls

4. Incluir URLs en `tribu_backend/urls.py`

### Migraciones

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver migraciones por app
python manage.py showmigrations
```

### Shell interactivo

```bash
python manage.py shell

# Importar modelos
from services.models import Service
from bookings.models import Booking
```

## 🔐 Seguridad

- SECRET_KEY en variables de entorno
- DEBUG=False en producción
- CORS configurado correctamente
- Validaciones en serializers
- HTTPS en producción

## 📚 Documentación Adicional

- [ESTRUCTURA.md](ESTRUCTURA.md) - Arquitectura detallada
- [API_DOCS.md](API_DOCS.md) - Documentación completa de API
- [DEPLOYMENT.md](DEPLOYMENT.md) - Guía de deployment

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Para problemas o consultas, abrir un issue en GitHub.

---

**Desarrollado con ❤️ para La Tribu**
