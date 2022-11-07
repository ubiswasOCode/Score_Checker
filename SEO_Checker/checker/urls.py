from django.urls import path,include
from checker.views import Score_checker, Selenium, Home

urlpatterns = [
    path('score_checker/', Score_checker,name="Score_checker"),
    path('selenium/', Selenium ,name="selenium"),
    path('', Home,name="Home"),

]

