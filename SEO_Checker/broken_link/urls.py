from django.urls import path,include
from broken_link.views import get_links_from_url


urlpatterns = [

    path('get_links_from_url/', get_links_from_url,name="get_links_from_url"),

]

