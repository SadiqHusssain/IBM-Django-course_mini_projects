from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('date-today', view=views.get_date, name='get_date'),
]