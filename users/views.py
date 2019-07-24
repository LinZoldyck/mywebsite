from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    template = 'users/register.html'
    if request.method =='POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Le compte pour {username} a été créé !')
           return redirect('blog:blog_index')
    else:
        form = UserRegisterForm()

    return render(request, template, {'form':form})
