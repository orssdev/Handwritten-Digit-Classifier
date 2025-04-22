from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random
import base64
import json

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

@csrf_exempt
def send_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data['image'].split(',')[1] 
        image_bytes = base64.b64decode(image_data)
        print(image_bytes.hex())
    data = []
    for i in range(10):
        data.append(random.randint(1, 100))
    return JsonResponse({'Numbers': data})