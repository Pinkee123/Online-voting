from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('register/',views.registration),
    path('uelection/',views.uelection),
    path('login/',views.login),
    path('vote/',views.voteforparty),

    ]