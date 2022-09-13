from django.urls import path,include
from broken_link import views


urlpatterns = [
    # path('get_links/', views.get_links_from_url,name="get_links_from_url"),
    path('base/', views.base,name="base"),
      
]

