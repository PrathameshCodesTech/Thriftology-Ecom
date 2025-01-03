from django.db import models
from django.contrib.auth.models import User



# Create your models here.

CATEGORY_CHOICE = (
    ('OW' , 'Outerwear'),
    ('T' , 'Top'),
    ('B' , 'Bottom'),
    ('CK' , 'ChicKicks'),
    ('A', 'Accessories'),
)

class Product(models.Model):
    brand = models.CharField(max_length=55)
    name = models.CharField(max_length=255)
    description = models.TextField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    image = models.ImageField(upload_to='products/')
    video = models.FileField(upload_to='products/videos/', blank=True, null=True) # New field for videos


    def __str__(self):
        return f'{self.name} ({self.brand})'
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
    
        