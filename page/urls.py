from django.urls import path
from . import views 
# urls of the app
app_name = 'page'
urlpatterns = [
    path('', views.index, name="page_index"),
    path('contact/', views.contact, name ="page_contact"),
    path('about/', views.about, name = "page_about"),
]