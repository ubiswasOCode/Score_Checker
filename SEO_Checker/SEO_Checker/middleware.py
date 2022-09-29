import http
from django.http import HttpResponseRedirect
class ChangeUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)
        domain = request.META['HTTP_HOST']
        if domain == "127.0.0.1:8000":
            return response
        
        elif request.path.startswith('/demo/seo-tool/') and domain == "www.psd2htmlx.com":
            return response
        else:
            return HttpResponseRedirect(f"/demo/seo-tool{request.path}")
        