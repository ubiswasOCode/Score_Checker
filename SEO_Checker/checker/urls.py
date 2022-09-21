from django.urls import path,include
from checker import views

urlpatterns = [
    path('score_checker/', views.Score_checker,name="Score_checker"),
    path('', views.Home,name="Home"),

    
    
    
]

