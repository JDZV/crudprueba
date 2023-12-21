# Importa funciones y clases necesarias de Django
from django.urls import path
from . import views

# Define las URL de la aplicación 'mi_aplicacion'
urlpatterns = [
    path('crear/', views.create_gps, name='crear_gps'),  # Ruta para crear un GPS
    path('ver/', views.get_gps, name='listar_gps'),  # Ruta para listar todos los GPS (sin identificador)
    path('ver/<int:gps_id>/', views.get_gps, name='ver_gps'),  # Ruta para ver un GPS específico (con identificador)
    path('actualizar/<int:gps_id>/', views.update_gps, name='actualizar_gps'),  # Ruta para actualizar un GPS
    path('eliminar/<int:gps_id>/', views.delete_gps, name='eliminar_gps'),  # Ruta para eliminar un GPS
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
    # Puedes agregar más rutas aquí según sea necesario
]
