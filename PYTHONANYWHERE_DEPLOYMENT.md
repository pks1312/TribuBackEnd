# 🚀 Guía de Deployment en PythonAnywhere

## 📋 Requisitos Previos

- Cuenta en PythonAnywhere (Gratis o de pago)
- Repositorio de GitHub actualizado
- Base de datos configurada (MySQL en PythonAnywhere)

---

## 🎯 PASO 1: Crear cuenta en PythonAnywhere

1. Ve a https://www.pythonanywhere.com/
2. Crea una cuenta gratuita o inicia sesión
3. Ve al Dashboard

---

## 🔧 PASO 2: Configurar la Aplicación Web

### 1. Crear Web App

1. En el Dashboard, ve a **"Web"**
2. Click en **"Add a new web app"**
3. Selecciona tu dominio: `tunombre.pythonanywhere.com`
4. Selecciona **"Manual configuration"** (NO Django wizard)
5. Selecciona **Python 3.10** o **Python 3.11**
6. Click **"Next"**

---

## 📦 PASO 3: Clonar el Repositorio

1. En el Dashboard, ve a **"Consoles"**
2. Abre una **"Bash console"**
3. Ejecuta estos comandos:

```bash
# Clonar el repositorio
git clone https://github.com/pks1312/TribuBackEnd.git

# Entrar al directorio
cd TribuBackEnd
```

---

## 🐍 PASO 4: Crear Virtual Environment

En la misma consola Bash:

```bash
# Crear virtualenv
mkvirtualenv --python=/usr/bin/python3.11 tribu-env

# Activar el virtualenv
workon tribu-env

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🗄️ PASO 5: Configurar Base de Datos MySQL

### 1. Crear base de datos

1. En el Dashboard, ve a **"Databases"**
2. En la sección **"MySQL"**, click en **"Initialize MySQL"** (si es primera vez)
3. Establece una contraseña para MySQL
4. Crea una nueva base de datos: `tunombre$tribu_db`

### 2. Anotar credenciales

```
Host: tunombre.mysql.pythonanywhere-services.com
Database: tunombre$tribu_db
Username: tunombre
Password: [tu-contraseña-mysql]
```

### 3. Instalar cliente MySQL

En la consola Bash:

```bash
workon tribu-env
pip install mysqlclient
```

---

## ⚙️ PASO 6: Configurar Variables de Entorno

Crea un archivo `.env` en el directorio del proyecto:

```bash
cd ~/TribuBackEnd
nano .env
```

Agrega estas variables:

```bash
SECRET_KEY=tu-secret-key-super-segura-aqui
DEBUG=False
ALLOWED_HOSTS=tunombre.pythonanywhere.com
DATABASE_URL=mysql://tunombre:tu-password-mysql@tunombre.mysql.pythonanywhere-services.com/tunombre$tribu_db
CORS_ALLOWED_ORIGINS=https://tribu-theta.vercel.app
```

Guarda con `Ctrl+O`, `Enter`, `Ctrl+X`

---

## 🔨 PASO 7: Ejecutar Migraciones

En la consola Bash:

```bash
cd ~/TribuBackEnd
workon tribu-env
python manage.py migrate
python manage.py collectstatic --no-input
```

---

## 🌐 PASO 8: Configurar WSGI File

1. En el Dashboard, ve a **"Web"**
2. En la sección **"Code"**, busca **"WSGI configuration file"**
3. Click en el link (algo como `/var/www/tunombre_pythonanywhere_com_wsgi.py`)
4. **Reemplaza TODO el contenido** con esto:

```python
import os
import sys
from dotenv import load_dotenv

# Agregar el directorio del proyecto al path
path = '/home/tunombre/TribuBackEnd'
if path not in sys.path:
    sys.path.append(path)

# Cargar variables de entorno
project_folder = os.path.expanduser('~/TribuBackEnd')
load_dotenv(os.path.join(project_folder, '.env'))

# Configurar Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'tribu_backend.settings'

# Importar la aplicación Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**IMPORTANTE:** Reemplaza `tunombre` con tu nombre de usuario de PythonAnywhere.

Guarda el archivo.

---

## 📁 PASO 9: Configurar Archivos Estáticos

1. En el Dashboard, ve a **"Web"**
2. En la sección **"Static files"**, agrega:

```
URL: /static/
Directory: /home/tunombre/TribuBackEnd/staticfiles
```

3. Agrega otra entrada para archivos media (futuro):

```
URL: /media/
Directory: /home/tunombre/TribuBackEnd/media
```

---

## 🎯 PASO 10: Configurar Virtual Environment en Web App

1. En el Dashboard, ve a **"Web"**
2. En la sección **"Virtualenv"**, busca el campo de texto
3. Ingresa la ruta completa de tu virtualenv:

```
/home/tunombre/.virtualenvs/tribu-env
```

---

## 🔄 PASO 11: Recargar la Aplicación

1. En el Dashboard, ve a **"Web"**
2. Arriba en verde, click en **"Reload tunombre.pythonanywhere.com"**
3. Espera unos segundos

---

## ✅ PASO 12: Verificar

Visita tu aplicación:

```
https://tunombre.pythonanywhere.com/health/
```

Deberías ver:
```json
{"status": "ok", "database": "connected", "message": "Backend funcionando correctamente"}
```

Prueba la API:
```
https://tunombre.pythonanywhere.com/api/services/
```

---

## 👤 PASO 13: Crear Superusuario

En la consola Bash:

```bash
cd ~/TribuBackEnd
workon tribu-env
python manage.py createsuperuser
```

Accede al admin:
```
https://tunombre.pythonanywhere.com/admin/
```

---

## 🔧 Troubleshooting

### Error 500
1. Ve a **"Web"** → **"Log files"** → **"Error log"**
2. Lee el error y corrige

### Base de datos no conecta
1. Verifica las credenciales en `.env`
2. Asegúrate de tener `mysqlclient` instalado
3. Verifica que el DATABASE_URL sea correcto

### Archivos estáticos no cargan
1. Ejecuta `python manage.py collectstatic --no-input`
2. Verifica la ruta en "Static files"
3. Recarga la aplicación

---

## 🔄 Actualizar el Código

Cuando hagas cambios:

```bash
cd ~/TribuBackEnd
git pull origin main
workon tribu-env
pip install -r requirements.txt  # Si hay nuevas dependencias
python manage.py migrate  # Si hay nuevas migraciones
python manage.py collectstatic --no-input
```

Luego en el Dashboard → Web → **Reload**

---

## 📊 Límites del Plan Gratuito

- 1 web app
- 512 MB de espacio en disco
- MySQL database (max 100 MB)
- Hibernación después de 3 meses sin actividad
- Subdominio: `tunombre.pythonanywhere.com`

Para producción seria, considera el plan de pago ($5/mes).

---

## 🎉 ¡Listo!

Tu backend Django está desplegado en PythonAnywhere.

**URL de producción:** `https://tunombre.pythonanywhere.com`

