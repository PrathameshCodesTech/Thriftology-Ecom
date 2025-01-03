from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    STATE_CHOICES = (
    ('Maharashtra', 'Maharashtra'),
    ('Gujarat', 'Gujarat'),
    ('Rajasthan', 'Rajasthan'),
    ('Karnataka', 'Karnataka'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Kerala', 'Kerala'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('West Bengal', 'West Bengal'),
    ('Bihar', 'Bihar'),
    ('Punjab', 'Punjab'),
    ('Haryana', 'Haryana'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Telangana', 'Telangana'),
    ('Odisha', 'Odisha'),
    ('Assam', 'Assam'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Jharkhand', 'Jharkhand'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)


    def __str__(self):
        return f'{self.name}-{self.city}'