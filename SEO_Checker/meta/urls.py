from django.urls import path,include
from meta import views
urlpatterns = [
    path('Meta/', views.Meta,name="Meta"),
    #  path('', views.Home,name="Home"),
    # path('Scra',views.Scraping,name='Scraping'),
]