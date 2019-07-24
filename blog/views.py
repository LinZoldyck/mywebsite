from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from . models import Post
# Create your views here.
class PostForm (ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'summary', 'date_posted', 'author']



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
