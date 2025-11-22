"""
WSGI config for PythonAnywhere deployment.

Copia el contenido de este archivo en el WSGI configuration file de PythonAnywhere.

IMPORTANTE: Reemplaza 'tunombre' con tu nombre de usuario de PythonAnywhere.
"""

import os
import sys
from dotenv import load_dotenv

# ============================================
# REEMPLAZA 'tunombre' CON TU USERNAME
# ============================================
USERNAME = 'tunombre'  # ← CAMBIA ESTO

# Agregar el directorio del proyecto al path
path = f'/home/{USERNAME}/TribuBackEnd'
if path not in sys.path:
    sys.path.append(path)

# Cargar variables de entorno desde .env
project_folder = os.path.expanduser(f'~/TribuBackEnd')
load_dotenv(os.path.join(project_folder, '.env'))

# Configurar Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'tribu_backend.settings'

# Importar y exponer la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

