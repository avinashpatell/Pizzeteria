from django.shortcuts import render
from .models import Pizza, Toppings

def index(request):
    """the home page for the Pizzeteria"""
    return render(request,'pizzeteria/index.html')

def pizza(request):
    pizzas=Pizza.objects.order_by('date_added')
    context={'pizzas':pizzas}
    return render(request,'pizzeteria/pizza_name.html',context)

def toppings(request, pizza_id):
    """Show toppings for a specific pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.all()  # Assuming a ForeignKey from Toppings to Pizza
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeteria/toppings.html', context)
