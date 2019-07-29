from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=100)
    #content = models.TextField()
    content = RichTextUploadingField(blank=True, null=True, config_name='default')
    summary = models.CharField(default="",max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
