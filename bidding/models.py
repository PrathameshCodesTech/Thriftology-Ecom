from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class NewArrival(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'New Arrival: {self.product.name}'

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_arrival = models.ForeignKey(NewArrival, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f'Bid by {self.user.username} for {self.new_arrival.product.name} - {self.amount}'