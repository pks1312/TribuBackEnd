# 🔧 Tribu Backend - Django REST API

API REST para la plataforma Tribu, construida con Django y Django REST Framework.

---

## 🚀 Quick Start

### Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/pks1312/TribuBackEnd.git
cd TribuBackEnd

# Crear virtual environment
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tus valores

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

El servidor estará en: `http://localhost:8000`

---

## 📁 Estructura

```
backend/
├── tribu_backend/        # Configuración principal de Django
├── accounts/             # Gestión de usuarios y perfiles
├── services/             # Servicios ofrecidos
├── professionals/        # Profesionales/empleados
├── schedules/            # Horarios de profesionales
├── bookings/             # Reservas de clientes
├── testimonials/         # Testimonios y reviews
├── gallery/              # Galería de imágenes
├── manage.py             # CLI de Django
└── requirements.txt      # Dependencias Python
```

---

## 🌐 API Endpoints

### Base URL
- **Local:** `http://localhost:8000`
- **Producción:** `https://tunombre.pythonanywhere.com`

### Endpoints Principales

```
GET  /api/services/           # Lista de servicios
POST /api/services/           # Crear servicio (auth)
GET  /api/services/{id}/      # Detalle de servicio

GET  /api/professionals/      # Lista de profesionales
POST /api/professionals/      # Crear profesional (auth)

GET  /api/schedules/          # Horarios disponibles
POST /api/schedules/          # Crear horario (auth)

GET  /api/bookings/           # Reservas del usuario
POST /api/bookings/           # Crear reserva (auth)

GET  /api/testimonials/       # Testimonios aprobados
POST /api/testimonials/       # Crear testimonio (auth)

GET  /api/gallery/            # Imágenes de galería

GET  /health/                 # Health check
GET  /admin/                  # Panel de administración
```

---

## 🗄️ Base de Datos

### Desarrollo
SQLite (por defecto)

### Producción (PythonAnywhere)
MySQL

Configuración en `.env`:
```bash
DATABASE_URL=mysql://user:pass@host/database
```

---

## 🔐 Autenticación

El API usa **Session Authentication** de Django.

Para endpoints protegidos, el usuario debe estar autenticado.

---

## 🚀 Deployment en PythonAnywhere

Ver guía completa: [`PYTHONANYWHERE_DEPLOYMENT.md`](PYTHONANYWHERE_DEPLOYMENT.md)

**Resumen rápido:**

1. Crear cuenta en PythonAnywhere
2. Clonar repositorio
3. Crear virtualenv e instalar dependencias
4. Configurar MySQL y variables de entorno
5. Ejecutar migraciones
6. Configurar WSGI file
7. Configurar archivos estáticos
8. Reload app

---

## 🛠️ Tecnologías

- **Django** 5.0.6
- **Django REST Framework** 3.15.2
- **django-cors-headers** 4.3.1
- **MySQL** (producción) / SQLite (desarrollo)
- **Python** 3.11

---

## 📝 Variables de Entorno

```bash
SECRET_KEY=tu-secret-key-aqui
DEBUG=False
ALLOWED_HOSTS=tunombre.pythonanywhere.com
DATABASE_URL=mysql://user:pass@host/database
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app
```

---

## 👨‍💻 Desarrollo

### Crear nueva app

```bash
python manage.py startapp nombre_app
```

### Crear migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Colectar archivos estáticos

```bash
python manage.py collectstatic
```

---

## 🔗 Enlaces

- **Repositorio:** https://github.com/pks1312/TribuBackEnd
- **Frontend:** https://github.com/pks1312/TribuFrontEnd
- **Producción:** https://tunombre.pythonanywhere.com

---

## 📄 Licencia

Privado
