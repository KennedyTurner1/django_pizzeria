from django.shortcuts import render

# Create your views here.

#when a URL request matches the url pattern in urls.py
#it looks for the function called index() in the views.py file

def index(request):
    #this is where the url request is processed
    return render(request, 'pizzas/index.html')
    #this sends the requesr back to the browser using an html template
    #that defines what the page will look like

from .models import Pizza

def pizzas(request):
    pizzas = Pizza.objects.all()
    #get all the pizza objects, Hawaiian and Meat Lovers

    context = {'pizzas':pizzas}
    #define the data we will pass to the skeleton html

    return render(request, 'pizzas/pizzas.html', context)
    #return the get request, send it to pizzas/pizzas.html
    #with the data of the available pizzas

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    #get the object associated with the id we requested
    toppings = pizza.topping_set.all()
    #access the foreign key by the entry_set function
    #list them all
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)
