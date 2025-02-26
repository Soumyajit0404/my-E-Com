from django.urls import path,include
#from django import views 
from . import views
#from shop import views

urlpatterns = [
    path("", views.index, name="bloghome")
]
