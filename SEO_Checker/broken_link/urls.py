from django.urls import path,include
from broken_link.views import get_links_from_url,all_links


urlpatterns = [

    path('get_links_from_url/', get_links_from_url,name="get_links_from_url"),
    path('all_links/', all_links,name="all_links"),

]

