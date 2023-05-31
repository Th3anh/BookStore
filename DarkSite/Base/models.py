from django.db import models
from User.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Book')
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    image = models.ImageField(upload_to='product', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.title



class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    
    def total_price(self):
        return self.book.price * self.quantity


class Cart(models.Model): 
    items = models.ManyToManyField(CartItem, null = True, blank = True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

