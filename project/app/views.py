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