# Importa funciones y clases necesarias de Django
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from .models import GPS, Sensores, Position
from django.core.serializers import serialize
from django.http import Http404
import json
import pandas as pd

# Vista para crear un nuevo GPS
@csrf_exempt
@require_POST
def create_gps(request):
    try:
        # Intenta cargar los datos del cuerpo de la solicitud como JSON
        data = json.loads(request.body.decode('utf-8'))

        # Crea instancias para Sensores y Position
        sensores_data = data.get('sensores', {})
        sensores_instance = Sensores.objects.create(**sensores_data)

        position_data = data.get('position', {})
        position_instance = Position.objects.create(**position_data)

        # Obtiene la fecha y hora actual
        fecha_hora_actual = timezone.now()

        # Crea la instancia del GPS con los datos proporcionados y la fecha y hora
        gps_data = {
            'imei': data.get('imei'),
            'position': position_instance,
            'alt': data.get('alt'),
            'speed': data.get('speed'),
            'orientation': data.get('orientation'),
            'sensores': sensores_instance,
            'fecha_hora': fecha_hora_actual  # Agrega la fecha y hora
        }

        gps_instance = GPS.objects.create(**gps_data)

        return JsonResponse({'id': gps_instance.id, 'message': 'GPS created'}, status=201)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')

# Vista para obtener detalles de un GPS o listar todos los GPS
@require_GET
def get_gps(request, gps_id=None):
    if gps_id is not None:
        try:
            gps_instance = GPS.objects.get(id=gps_id)
            gps_data = {
                'id': gps_instance.id,
                'imei': gps_instance.imei,
                'position': {
                    'lat': gps_instance.position.lat,
                    'lon': gps_instance.position.lon,
                },
                'alt': gps_instance.alt,
                'speed': gps_instance.speed,
                'orientation': gps_instance.orientation,
                'sensores': {
                    'acc': gps_instance.sensores.acc,
                    'di1': gps_instance.sensores.di1,
                    'towing': gps_instance.sensores.towing,
                },
                'fecha_hora': gps_instance.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')  # Agrega la fecha y hora formateada
            }
            return JsonResponse({'data': gps_data})
        except GPS.DoesNotExist:
            raise Http404("GPS does not exist")
    else:
        gps_instances = GPS.objects.all()
        gps_list = [
            {
                'id': gps.id,
                'imei': gps.imei,
                'position': {
                    'lat': gps.position.lat,
                    'lon': gps.position.lon,
                },
                'alt': gps.alt,
                'speed': gps.speed,
                'orientation': gps.orientation,
                'sensores': {
                    'acc': gps.sensores.acc,
                    'di1': gps.sensores.di1,
                    'towing': gps.sensores.towing,
                },
                'fecha_hora': gps.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')  # Agrega la fecha y hora formateada
            }
            for gps in gps_instances
        ]
        return JsonResponse({'data': gps_list})

# Vista para actualizar un GPS existente
@csrf_exempt
@require_http_methods(["PUT"])
def update_gps(request, gps_id):
    try:
        gps_instance = GPS.objects.get(id=gps_id)
    except GPS.DoesNotExist:
        return JsonResponse({'error': 'GPS not found'}, status=404)

    try:
        data = json.loads(request.body.decode('utf-8'))

        # Actualiza campos generales
        gps_instance.imei = data.get('imei', gps_instance.imei)
        gps_instance.alt = data.get('alt', gps_instance.alt)
        gps_instance.speed = data.get('speed', gps_instance.speed)
        gps_instance.orientation = data.get('orientation', gps_instance.orientation)

        # Actualiza la posición
        position_data = data.get('position', {})
        position_instance = gps_instance.position
        position_instance.lat = position_data.get('lat', position_instance.lat)
        position_instance.lon = position_data.get('lon', position_instance.lon)
        position_instance.save()

        # Actualiza los sensores
        sensores_data = data.get('sensores', {})
        gps_instance.sensores.acc = sensores_data.get('acc', gps_instance.sensores.acc)
        gps_instance.sensores.di1 = sensores_data.get('di1', gps_instance.sensores.di1)
        gps_instance.sensores.towing = sensores_data.get('towing', gps_instance.sensores.towing)

        # Actualiza la fecha y hora a la actual
        gps_instance.fecha_hora = timezone.now()

        # Guarda el objeto actualizado
        gps_instance.save()

        return JsonResponse({'message': 'GPS updated'})
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON data')


# Vista para eliminar un GPS existente
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_gps(request, gps_id):
    try:
        # Intenta obtener el GPS existente y eliminarlo
        gps_instance = GPS.objects.get(id=gps_id)
    except GPS.DoesNotExist:
        raise Http404("GPS does not exist")

    gps_instance.delete()

    return JsonResponse({'message': 'GPS deleted'})

def exportar_excel(request):
    # Obtener datos de todos los GPS (ajusta esta lógica según tu necesidad)
    gps_instances = GPS.objects.all()

    # Crear un DataFrame de Pandas con los datos
    data = {
        'ID': [gps.id for gps in gps_instances],
        'IMEI': [gps.imei for gps in gps_instances],
        'Latitud': [gps.position.lat for gps in gps_instances],
        'Longitud': [gps.position.lon for gps in gps_instances],
        'Altitud': [gps.alt for gps in gps_instances],
        'Velocidad': [gps.speed for gps in gps_instances],
        'Orientacion': [gps.orientation for gps in gps_instances],
        'Acc': [gps.sensores.acc for gps in gps_instances],
        'Di1': [gps.sensores.di1 for gps in gps_instances],
        'Towing': [gps.sensores.towing for gps in gps_instances],
        'Fecha_Hora': [gps.fecha_hora.strftime('%Y-%m-%d %H:%M:%S') if gps.fecha_hora else '' for gps in gps_instances],
    }

    df = pd.DataFrame(data)

    # Crear una respuesta de Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=gps_data.xlsx'

    # Guardar el DataFrame en el archivo Excel
    df.to_excel(response, index=False)

    return response