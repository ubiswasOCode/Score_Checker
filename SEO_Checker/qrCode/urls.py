from django.urls import path,include
from qrCode import views
urlpatterns = [
    path('QRCode/', views.QRCode,name="QRCode"),
    
]