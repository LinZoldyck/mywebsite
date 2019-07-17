from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'page/index.html'

    return render (request, template)

    