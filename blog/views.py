from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from blog.forms import PostForm
from blog.models import Post


# Create your views here.
def index(request):
    return HttpResponseRedirect('/hello/')

def create(request):
    form = PostForm()
    return render(request, "create.html", {"form": form})

def save(request):
    form = PostForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        date = form.cleaned_data["date"]
        post = Post(title=title, content=content, date=date)
        post.save()
        return HttpResponseRedirect('/blog')

def list(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})
