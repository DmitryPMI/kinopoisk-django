from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name = 'Index'),
    path('index1', views.index1, name = 'Index'),
]
