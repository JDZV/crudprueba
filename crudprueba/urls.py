# Importa las funciones necesarias de Django para manejar URL
from django.contrib import admin
from django.urls import path, include

# Define las URL del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración de Django
    path('mi_aplicacion/', include('mi_aplicacion.urls')),  # Incluye las URL de la aplicación 'mi_aplicacion'
    # Puedes agregar otras URL de la aplicación 'crudprueba' o cualquier otra aquí
]
