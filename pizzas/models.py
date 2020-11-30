from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        #this is a string method
        #this returns the class Pizza's attribute name
        #returns something useful instead of garbage

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #makes a connection, 1 pizza can have many toppings
    name = models.CharField(max_length=200)
    #we do not need a textbox but a character box 

    def __str__(self):
        return self.name