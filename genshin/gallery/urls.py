from django.urls import path
from . import views


urlpatterns = [
    path('', views.pers, name='pers'),
]
