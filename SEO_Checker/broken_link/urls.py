from django.urls import path,include
from broken_link import views


urlpatterns = [
    # path('get_links/', views.get_links_from_url,name="get_links_from_url"),
    path('broken_link/', views.get_links_from_url,name="get_links_from_url"),
      
]

