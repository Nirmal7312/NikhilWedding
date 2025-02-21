from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings  # Correct way to import settings
def index(request):
    ti = 160
    images = [f'img({i}).jpg' for i in range(1, ti + 1)]
    for img in images:
        print(img)
    params = {'images':images}
    return render(request, 'index.html', params)

def view_img(request, img_name):
    params = {'img_name':img_name}
    return render(request, 'view.html', params)