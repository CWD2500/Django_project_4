from django.http.response import HttpResponse

def homPage(request):
    return HttpResponse("Hello Django :) ...! ")
