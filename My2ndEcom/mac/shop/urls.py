from django.urls import path,include
#from django import views 
from . import views
#from shop import views

urlpatterns = [
    path("", views.index, name="shophome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productView/", views.prodView, name="ProdView"),
    path("checkout/", views.checkout, name="Checkout"),
]
