from django.urls import path,include
from checker import views
urlpatterns = [
    path('score_checker/', views.Score_checker,name="Score_checker"),
    # path('Get_Density_Check', views.Get_Density_Check,name="Get_Density_Check"),
    
]