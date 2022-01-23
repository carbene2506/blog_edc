from django.urls import path
from . import views

urlpatterns = [
    
    #path('',"nice"),
    path('create/', views.create_blog),
    path('display', views.display_blogs)
]