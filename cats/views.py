import random
from django.http import JsonResponse
from .models import CatImage

def random_cat_image(request):
    cat = random.choice(CatImage.objects.all())
    response = {"source": cat.image.url}
    return JsonResponse(response)

def random_cat_images(request, count):
    count = int(count)
    cats = random.sample(list(CatImage.objects.all()), count)
    response = {"source": [cat.image.url for cat in cats]}
    return JsonResponse(response)

from django.shortcuts import render
from .models import CatImage

def index(request):
    cats = CatImage.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

