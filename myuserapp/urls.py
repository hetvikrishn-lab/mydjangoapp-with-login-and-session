from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview),
    path('home',views.homepageview),
    path('about',views.aboutpageview), 
    path('contact',views.contactpageview),
    path('contactprocess',views.contactprocess),
    path('cake',views.contactpageview),
    path('cake/ahmedabad',views.contactpageview),
    path('cake/rajkot',views.contactpageview),
    path('shop',views.shoppage), 
    path('saveSession',views.saveSessionData),
    path('getSession',views.getSessionData),
    path('getSession2',views.getSessionData2), 
    path('removeSession',views.deleteSessionData),
    path('login',views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
]