from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name = 'Index'),
    path('index1', views.index1, name = 'Index'),
    path('base', views.base, name = 'Index'),
    path('<int:film_id>/', views.film, name='film')
]
