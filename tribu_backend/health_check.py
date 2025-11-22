from django.http import JsonResponse
from django.db import connection


def health_check(request):
    """Health check endpoint para verificar el estado del servidor"""
    try:
        # Verificar conexión a la base de datos
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        return JsonResponse({
            'status': 'ok',
            'database': 'connected',
            'message': 'Backend funcionando correctamente'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'database': 'disconnected',
            'error': str(e)
        }, status=500)


def debug_info(request):
    """Información de debug para diagnosticar problemas"""
    from django.apps import apps
    
    installed_apps = [app.name for app in apps.get_app_configs()]
    
    tables_info = {}
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema='public'
            """)
            tables = [row[0] for row in cursor.fetchall()]
            tables_info = {'tables': tables, 'count': len(tables)}
    except Exception as e:
        tables_info = {'error': str(e)}
    
    return JsonResponse({
        'installed_apps': installed_apps,
        'database_info': tables_info,
        'debug_mode': False
    })

