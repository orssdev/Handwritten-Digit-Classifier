from django.shortcuts import render
from django.http import HttpResponse
import json
import random
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def send_test(request):
    data = []
    for i in range(10):
        data.append(random.randint(1, 100))
    return JsonResponse({'Numbers': data})

def send_prediction(request):
    data = ""
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        # Here you would typically process the data and return a prediction
        # For now, we will just return the data back as a response
        return JsonResponse({'prediction': data})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)