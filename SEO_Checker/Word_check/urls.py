from django.urls import path,include
from Word_check import views
urlpatterns = [
    path('Word_Count/', views.Word_Count,name="Word_Count"),
    #  path('', views.Home,name="Home"),
    # path('Scra',views.Scraping,name='Scraping'),
]