from django.urls import path,include
from .views import Density_Check

urlpatterns = [
    path('density/', Density_Check, name="density"), 
    
]