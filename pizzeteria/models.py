from django.db import models

# Create your models here.

class Pizza(models.Model):
    name=models.TextField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Toppings(models.Model):
    pizza=models.ForeignKey(Pizza,on_delete=models.PROTECT)
    name=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name