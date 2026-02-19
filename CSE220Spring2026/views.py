from django.http import HttpResponse, Http404
from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html', {'language': 'C++', 'message': 'Hello World!'})

def X(request, id):
    id = id + 1000
    return HttpResponse(id)

def Y(request):
    raise Http404('Y')