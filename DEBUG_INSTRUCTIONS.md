# Instrucciones para habilitar DEBUG en Render

## Paso 1: Agregar variable de entorno

1. Ve al dashboard de Render
2. Click en tu servicio "tribu-backend"
3. Ve a **Settings** → **Environment**
4. Busca la variable `DEBUG` (o créala)
5. Cambia su valor a: `True`
6. Click en "Save Changes"

## Paso 2: Esperar el redeploy

Render redespliegará automáticamente.

## Paso 3: Probar nuevamente

Visita: https://tribubackend.onrender.com/api/services/

Ahora verás el error completo en la pantalla.

## Paso 4: Copiar el error

Copia todo el traceback del error y pégalo para poder solucionarlo.

---

**IMPORTANTE:** Después de solucionar el error, DEBES volver a poner `DEBUG=False`

