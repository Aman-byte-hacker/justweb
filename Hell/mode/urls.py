from django.contrib import admin
from django.urls import path
from mode import views
urlpatterns = [
  
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path('contact',views.contact,name="contact"),
    path('login/',views.loginusr,name="login"),
    path('login',views.loginusr,name="login"),
    path('register/',views.register,name="register"),
    path('register',views.register,name="register"),
    path('terms/',views.terms,name="terms"),
    path('terms',views.terms,name="terms")

]