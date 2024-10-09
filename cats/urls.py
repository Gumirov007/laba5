from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('random/', views.random_cat_image),
    path('random/<int:count>/', views.random_cat_images),
]

