# Guía de Deployment - Tribu Backend

## Deployment en Render

### Paso 1: Preparar el Repositorio

1. Asegúrate de que todos los archivos estén comiteados en el repositorio:
```bash
git add .
git commit -m "Backend Django listo para deployment"
git push origin main
```

### Paso 2: Crear Base de Datos en Render

1. Ve a [Render Dashboard](https://dashboard.render.com/)
2. Clic en "New +" → "PostgreSQL"
3. Configuración:
   - **Name**: `tribu-db`
   - **Plan**: Free
   - **Region**: Oregon (US West) o el más cercano
4. Clic en "Create Database"
5. **IMPORTANTE**: Guarda la URL de conexión (Internal Database URL)

### Paso 3: Crear Web Service

1. En Render Dashboard, clic en "New +" → "Web Service"
2. Conecta tu repositorio de GitHub: `https://github.com/pks1312/TribuBackEnd`
3. Configuración:
   - **Name**: `tribu-backend`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: Dejar vacío (o `.` si es necesario)
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn tribu_backend.wsgi:application`
   - **Plan**: Free

### Paso 4: Configurar Variables de Entorno

En la sección "Environment Variables", agregar:

```bash
SECRET_KEY=<generar-una-clave-secreta-aleatoria>
DEBUG=False
ALLOWED_HOSTS=.onrender.com,tribu-backend.onrender.com
DATABASE_URL=<internal-database-url-from-step-2>
CORS_ALLOWED_ORIGINS=https://tribu-theta.vercel.app,https://www.tudominio.com
```

**Para generar SECRET_KEY** (ejecutar en Python):
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Paso 5: Deploy

1. Clic en "Create Web Service"
2. Render automáticamente:
   - Instalará dependencias
   - Ejecutará migraciones
   - Recolectará archivos estáticos
   - Iniciará el servidor

### Paso 6: Verificar Deployment

1. Espera a que termine el build (puede tomar 5-10 minutos)
2. Visita: `https://tribu-backend.onrender.com/api/`
3. Deberías ver la lista de endpoints de la API

### Paso 7: Crear Superusuario

1. Ve a la pestaña "Shell" en tu servicio de Render
2. Ejecuta:
```bash
python manage.py createsuperuser
```
3. Sigue las instrucciones para crear el usuario admin

### Paso 8: Acceder al Admin

Visita: `https://tribu-backend.onrender.com/admin/`

## Endpoints Disponibles

- `GET /api/services/` - Lista de servicios
- `GET /api/professionals/` - Lista de profesionales
- `GET /api/schedules/` - Horarios disponibles
- `POST /api/bookings/` - Crear reserva
- `GET /api/testimonials/` - Testimonios aprobados
- `GET /api/gallery/` - Imágenes de galería

## Mantenimiento

### Actualizar el Backend

```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

Render detectará los cambios y desplegará automáticamente.

### Ver Logs

En el dashboard de Render, ve a tu servicio y clic en "Logs" para ver los registros en tiempo real.

### Ejecutar Migraciones Manualmente

Si necesitas ejecutar migraciones manualmente:

1. Ve a "Shell" en el dashboard
2. Ejecuta:
```bash
python manage.py migrate
```

## Troubleshooting

### Error: "Application failed to start"
- Revisa los logs en Render
- Verifica que todas las variables de entorno estén configuradas
- Asegúrate de que `build.sh` tenga permisos de ejecución

### Error de Base de Datos
- Verifica que DATABASE_URL esté correctamente configurada
- Asegúrate de que la base de datos esté en la misma región

### Error de CORS
- Verifica que CORS_ALLOWED_ORIGINS incluya la URL de tu frontend
- No olvides incluir el protocolo (https://)

## Seguridad

⚠️ **IMPORTANTE**:
- Nunca subas archivos `.env` al repositorio
- Mantén SECRET_KEY segura
- En producción, siempre usa `DEBUG=False`
- Usa HTTPS en producción
- Configura ALLOWED_HOSTS correctamente

