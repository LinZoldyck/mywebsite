from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name = 'blog_index'),
    path('view/<int:pk>', views.detail, name = 'blog_view'),
    path('new', views.create, name='blog_create')
]