from django.urls import path
from . import views 
# urls of the app

urlpatterns = [
    path('', views.index, name="page_index"),

]