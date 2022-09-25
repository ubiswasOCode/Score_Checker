from django.urls import path,include
from ChangeCase import views


urlpatterns = [
    path('ChangeCase/', views.ChangeCase,name="ChangeCase"),
      
]

