from django.http import HttpResponse, Http404
from django.shortcuts import render


def hello(request):
    raise Http404()
    return render(request, 'hello.html')