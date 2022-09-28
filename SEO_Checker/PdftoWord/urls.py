from django.urls import path,include
from PdftoWord import views
urlpatterns = [
    path('PdftoWord/', views.PdftoWord,name="PdftoWord"),
    
]