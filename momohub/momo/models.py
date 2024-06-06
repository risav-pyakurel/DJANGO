from django.db import models
from django.utils import timezone
# Create your models here.

class MomoVarity(models.Model):
    MOMO_TYPE_CHOICE= [
        ('SM', 'STEAM MOMO')
        ('FM','Fried MOMO')
        ('CM', 'Chilliy MOMO')
    ]
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='momo/')
    date_added = models.DateTimeField(default= timezone.now)
    type=  models.CharField(max_length= 2,choices= MOMO_TYPE_CHOICE)

