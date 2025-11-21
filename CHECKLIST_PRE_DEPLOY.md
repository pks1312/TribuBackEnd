# ✅ Checklist Pre-Deploy - Backend

Verifica cada item ANTES de hacer deploy a Render.

## 📋 Configuración

- [ ] Archivo `.env.example` existe y está actualizado
- [ ] Archivo `.gitignore` incluye `.env`, `venv/`, `__pycache__/`, `*.pyc`
- [ ] `settings.py` usa variables de entorno para secrets
- [ ] `DEBUG` usa variable de entorno (default False)
- [ ] `SECRET_KEY` usa variable de entorno
- [ ] `ALLOWED_HOSTS` configurado correctamente
- [ ] `CORS_ALLOWED_ORIGINS` usa variable de entorno
- [ ] Base de datos configurada con `dj_database_url`

## 🗄️ Base de Datos

- [ ] Migraciones generadas: `python manage.py makemigrations`
- [ ] Migraciones aplicadas localmente: `python manage.py migrate`
- [ ] Modelos tienen `verbose_name` y `verbose_name_plural`
- [ ] No hay conflictos de migraciones

## 🔐 Seguridad

- [ ] No hay archivos `.env` en el repositorio
- [ ] No hay `SECRET_KEY` hardcodeada en el código
- [ ] No hay credenciales en el código
- [ ] `DEBUG=False` en producción
- [ ] CORS configurado para dominios específicos
- [ ] HTTPS forzado en producción

## 📦 Dependencias

- [ ] `requirements.txt` actualizado y completo
- [ ] Todas las dependencias probadas localmente
- [ ] `Pillow` incluido (para ImageField)
- [ ] `psycopg2-binary` incluido (para PostgreSQL)
- [ ] `gunicorn` incluido (para servidor)
- [ ] `whitenoise` incluido (para archivos estáticos)

## 📁 Archivos de Deploy

- [ ] `build.sh` existe y tiene el contenido correcto
- [ ] `build.sh` tiene permisos de ejecución
- [ ] `Procfile` existe con comando correcto
- [ ] `runtime.txt` especifica versión de Python
- [ ] `render.yaml` configurado (opcional pero recomendado)

## 🧪 Testing Local

- [ ] Servidor Django inicia sin errores: `python manage.py runserver`
- [ ] Admin accesible en `/admin/`
- [ ] API responde en `/api/`
- [ ] Todos los endpoints funcionan
- [ ] CORS funciona con frontend local
- [ ] Archivos estáticos se sirven correctamente

## 📊 Modelos y Admin

- [ ] Todos los modelos registrados en admin
- [ ] Admin personalizado configurado
- [ ] `__str__()` definido en todos los modelos
- [ ] Campos apropiados en `list_display`
- [ ] `search_fields` configurados
- [ ] `list_filter` configurados

## 🔗 URLs

- [ ] URLs principales configuradas en `tribu_backend/urls.py`
- [ ] URLs de cada app incluidas
- [ ] `/admin/` funciona
- [ ] `/api/` incluye todas las apps
- [ ] No hay URLs duplicadas

## 📝 Documentación

- [ ] README.md actualizado
- [ ] API_DOCS.md existe
- [ ] Variables de entorno documentadas
- [ ] Instrucciones de instalación claras

## 🚀 Git

- [ ] `.gitignore` configurado correctamente
- [ ] Commit inicial hecho
- [ ] Mensajes de commit descriptivos
- [ ] Branch `main` configurado
- [ ] No hay archivos sensibles en el repo

## 🌐 Variables de Entorno para Render

Preparar estos valores:

```bash
SECRET_KEY=<generar-nueva>
DEBUG=False
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=<copiar-de-postgresql>
CORS_ALLOWED_ORIGINS=https://tribu-theta.vercel.app
```

## ✅ Comando Final de Verificación

```bash
# Ejecutar TODOS estos comandos sin errores
python manage.py check
python manage.py makemigrations --dry-run
python manage.py migrate --plan
python manage.py collectstatic --noinput
python manage.py test
```

## 📞 Si Todo Está ✅

Estás listo para:
1. Hacer push a GitHub
2. Crear database en Render
3. Crear web service en Render
4. Configurar variables de entorno
5. Deploy!

---

**Fecha de verificación:** _____________

**Verificado por:** _____________

**Notas adicionales:**

