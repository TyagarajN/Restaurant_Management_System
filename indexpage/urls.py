from django.urls import path
from . import views

#url routing is done here
urlpatterns = [
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact')
    path('about/', views.about,name='about.html')
    path('login/',views.login, name='login.html')
    path('registration/',views.registration, name='regis.html')
]