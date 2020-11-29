from django.shortcuts import render

# Create your views here.

#when a URL request matches the url pattern in urls.py
#it looks for the function called index() in the views.py file

def index(request):
    #this is where the url request is processed
    return render(request, 'pizzas/index.html')
    #this sends the requesr back to the browser using an html template
    #that defines what the page will look like