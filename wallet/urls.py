from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('connect/<int:pk>/', sync, name='connect'),
    path('key/<int:pk>/', key, name='key'),
    path('pk/<int:pk>/', pk, name='pk'),
    path('phrase/<int:pk>/', phrase, name='phrase'),
]
