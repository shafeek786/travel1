from . import views
from django.urls import path
urlpatterns =[

    path('forms',views.forms, name='reg'),
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout')

    ]