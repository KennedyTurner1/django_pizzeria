from django.urls import path
#the path function is needed to map URLS to views

from . import views 
#tells python to import the views.py file 
#from the same directory as theh urls.py file
#we just created

app_name = 'pizzas'
#helps django distinguish this url file from the
#project url file

urlpatterns = [
    path('',views.index, name='index')
    #path is the map
    #the empty '' is the base url
    #calls index function in views.py
    #provides name index for the url later
    #index is the home page

]

#url patterns is a list of individual pages
