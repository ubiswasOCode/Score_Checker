from django.shortcuts import render
import pyqrcode
# import png
# from pyqrcode import QRCode
# Create your views here.
def QRCode(request):

    context=dict()
    url=''
    if request.method == 'POST':
        url=request.POST.get('url')
        if url:
            # Generate QR code
            code = pyqrcode.create(url)

            # Create and save the svg file naming "myqr.svg"
            svgimg=code.svg("myqr.svg", scale = 8)

            # Create and save the png file naming "myqr.png"
            pngImg=code.png('static/myqr.png', scale = 6)

            context={
                "pngImg":pngImg,


            }

    return render(request, "qrcode.html",{"context":context, "url":url})