#!/bin/bash

# Script de setup automático para el backend de Tribu

echo "🚀 Iniciando setup del backend de Tribu..."

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python -m venv venv

# Activar entorno virtual
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Crear archivo .env si no existe
if [ ! -f .env ]; then
    echo "📝 Creando archivo .env..."
    cp .env.example .env
    echo "⚠️  Por favor, configura las variables de entorno en el archivo .env"
fi

# Ejecutar migraciones
echo "🗄️  Ejecutando migraciones..."
python manage.py migrate

# Recolectar archivos estáticos
echo "📂 Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo ""
echo "✅ Setup completado!"
echo ""
echo "Próximos pasos:"
echo "1. Configurar variables de entorno en .env"
echo "2. Crear superusuario: python manage.py createsuperuser"
echo "3. Iniciar servidor: python manage.py runserver"
echo ""

