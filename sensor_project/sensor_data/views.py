from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
THRESHOLD_VALUE = 2000

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all().order_by('-timestamp')
    serializer_class = SensorDataSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data

        if data['value'] > THRESHOLD_VALUE:
            return Response({"message": "Alert! Value exceeds threshold", "blink": True}, status=status.HTTP_201_CREATED)
        
        return response

@csrf_exempt
def blink_led(request):
    if request.method == 'POST':
        # Send a request to the ESP8266 (Arduino)
        url = 'http://192.168.147.113/blink-led'  # ESP8266 IP
        try:
            response = requests.post(url)  # Make sure this is a POST request
            if response.status_code == 200:
                return JsonResponse({'status': 'success', 'message': 'LED blinked'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Failed to blink LED'}, status=500)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    return Response({'status': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

import matplotlib.pyplot as plt
import io
from django.http import HttpResponse
from .models import SensorData

def plot_graph(request):
    data = SensorData.objects.all().order_by('-timestamp')[:10]
    values = [d.value for d in data]
    timestamps = [d.timestamp.strftime("%H:%M") for d in data]

    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.bar(timestamps, values)

    # Format the graph
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Sensor Value')
    ax.set_title('Sensor Data over Time')

    # Convert plot to PNG image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Serve the image as HTTP response
    return HttpResponse(buf, content_type='image/png')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests  # This will be used to send requests to the ESP8266
import json

@csrf_exempt  # Disable CSRF protection for simplicity (not recommended for production without token auth)
def control_fan(request):
    if request.method == 'POST':
        # Parse the request body
        data = json.loads(request.body)
        state = data.get('state')
        
        if state not in ['on', 'off']:
            return JsonResponse({'error': 'Invalid state'}, status=400)

        # Forward the state to the ESP8266
        try:
            esp_url = f"http://198.168.147.95/control-fan?state={state}"
            response = requests.get(esp_url)

            # Check if the request to the ESP8266 was successful
            if response.status_code == 200:
                return JsonResponse({'status': f'Fan is turned {state}'})
            else:
                return JsonResponse({'error': 'Failed to communicate with ESP8266'}, status=500)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': 'Error connecting to ESP8266', 'details': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=405)


