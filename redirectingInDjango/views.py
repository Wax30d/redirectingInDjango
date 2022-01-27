from django.http import HttpResponse


def index(request):
    html = """ <h1> Django Baby </h1> Hello, you just configured you First URL"""
    return HttpResponse(html)
