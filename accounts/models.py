from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    profile_pic=models.ImageField(default='default.png', null=True, blank=True)
    

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name        

class Product(models.Model):
    CATEGORY = (
        ('Breakfast ', 'Завтрак'),
        ('Lunch', 'Обед'),
        ('Dinner', 'Ужин')
    )
    name=models.CharField(max_length=200, null=True)
    price=models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description=models.CharField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name    




class Order(models.Model):
    STATUS = (
        ('Pending', 'Обрабатывается'),
        ('Out of delivery', 'Доставка'),
        ('Delivered', 'Доставленно')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
    note=models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.product.name    