from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Master(models.Model):
    name = models.CharField("Nom", max_length=250)
    age = models.DateField(auto_now_add = True)
    location = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)
    motto = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)

    def __str__ (self):
        return self.name

class Education(models.Model):
    master = models.ForeignKey(Master, on_delete = models.CASCADE)
    diploma = models.CharField("Diplôme", max_length = 500)
    start_date = models.DateField()
    end_date = models.DateField()
    school_logo = models.ImageField(upload_to = "images/")
    cursus_status = models.CharField(max_length=7)

    def __str__(self):
        return '%s %s' % (self.diploma, str(self.start_date))

class ProExperience(models.Model):
    master = models.ForeignKey(Master, on_delete = models.CASCADE)
    company_name = models.CharField("Entreprise", max_length= 100)
    company_logo = models.ImageField(upload_to = "images/")
    function = models.CharField("Poste occupée", max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '%s' % (self.company_name)

class Citation(models.Model):
    citation = models.CharField(max_length = 500)
    

