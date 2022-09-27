from django.urls import path,include
from ImagetoTxt import views
urlpatterns = [
    path('ImgtoTxt/', views.ImgtoTxt,name="ImgtoTxt"),
    #  path('', views.Home,name="Home"),
    # path('Scra',views.Scraping,name='Scraping'),
]