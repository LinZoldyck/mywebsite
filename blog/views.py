from django.shortcuts import render, get_object_or_404
from . models import Post
# Create your views here.

def index(request):
    template = 'blog/index.html'
    context = {
        'Posts':Post.objects.all()
    }
    return render(request, template, context)

def detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post,pk =pk)
    context = {
        'post': post
    }

    return render(request, template, context)