from django.urls import path, include

from . import views #write our own view for registration

app_name = 'users'

urlpatterns = [
    #include default urls 
    path('',include('django.contrib.auth.urls')),
    #registration page
    path('register/', views.register, name='register'), #use django's form, but we create our own view and template
]