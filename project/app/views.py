from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random
import base64
import json
from .digit_model import predict_digit

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

@csrf_exempt
def send_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data['image'].split(',')[1] 
        image_bytes = base64.b64decode(image_data)

        result = predict_digit(image_bytes)
    
        return JsonResponse(result)
    return JsonResponse({"error": "Invalid request method."})

def camera(request):
    return render(request, 'app/camera.html')