from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from . models import Post
from . forms import PostForm
# Create your views here.

def index(request):
    template = 'blog/index.html'
    context = {
        'Posts': Post.objects.all()
    }
    return render(request, template, context)

def detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post,pk =pk)
    context = {
        'post': post
    }
    return render(request, template, context)

def create(request):
    template = 'blog/form.html'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_index')
    else:
        form = PostForm()
    
    return render(request, template, {'form': form})
    