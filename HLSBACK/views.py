from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse

def index(request, *args, **kwargs):
    # Serve index.html from the dist folder (Vite build)
    index_path = os.path.join(settings.BASE_DIR, 'static','dist', 'index.html')
    with open(index_path, 'r') as file:
        return HttpResponse(file.read())
