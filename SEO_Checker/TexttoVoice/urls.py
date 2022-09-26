from django.urls import path,include
from TexttoVoice import views
urlpatterns = [
    path('TexttoVoice/', views.TexttoVoice,name="TexttoVoice"),
    #  path('', views.Home,name="Home"),
    # path('Scra',views.Scraping,name='Scraping'),
]