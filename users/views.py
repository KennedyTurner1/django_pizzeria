# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from  django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):

    if request.method != 'POST':
        form = UserCreationForm() #form made by django to create users
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            #new user is now an object
            new_user = form.save()
            #log the user in and redirect them to the home page
            login(request, new_user)
            return redirect('pizzas:index')

    context = {'form':form}

    return render(request, 'registration/register.html', context)




