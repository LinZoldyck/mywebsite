from django.shortcuts import render
from . models import Master, Education, ProExperience, Citation
# Create your views here.

def index(request):
    template = 'page/index.html'

    master = Master.objects.get(pk=1)
    Educations = Education.objects.all()
    ProExperiences = ProExperience.objects.all()
    citation = Citation.objects.get(pk=1)

    context = {
        'master': master,
        'Educations': Educations,
        'ProExperiences': ProExperience,
        'citation':citation,
    }
    return render (request, template, context)

def about(request):
    template = 'page/about.html'
    return render(request, template)

def contact(request):
    template = 'page/contact.html'
    return render(request, template)