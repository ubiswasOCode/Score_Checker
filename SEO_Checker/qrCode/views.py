from django.shortcuts import render
import pyqrcode
# import png
# from pyqrcode import QRCode
# Create your views here.
def QRCode(request):
    context=dict()
    if request.method == 'POST':
        url=request.POST.get('url')
        if url:    
            # Generate QR code
            url = pyqrcode.create(url)
            
            # Create and save the svg file naming "myqr.svg"
            svgimg=url.svg("myqr.svg", scale = 8)
            
            # Create and save the png file naming "myqr.png"
            pngImg=url.png('static/myqr.png', scale = 6) 
                    
            context={
                "pngImg":pngImg
            }
        
    return render(request, "base.html",context)