from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData
import json

@csrf_exempt
def save_sensor_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        # Save the data in the database
        sensor_data = SensorData(temperature=temperature, humidity=humidity)
        sensor_data.save()

        return JsonResponse({'status': 'success', 'message': 'Data saved successfully'})

    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)
def sensor_chart(request):
    # Sample data to be passed to the template
    context = {
        'temperature_data': [22, 23, 24],  # Dummy temperature data
        'humidity_data': [50, 55, 60],     # Dummy humidity data
        'timestamps': ['10:00', '10:01', '10:02']  # Sample timestamps
    }
    return render(request, 'sensor_data/chart.html', context)