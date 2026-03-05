from django.http import HttpResponse, Http404
from django.shortcuts import render

def main(request):
    return render(request, "base.html")

def hello(request):
    return render(request, 'hello.html',
                  {'blog_entries': ["Technology", "Healthcare", "Sports"]})

def X(request, id):
    id = id + 1000
    return HttpResponse(id)

def Y(request):
    raise Http404('We could not find that page')