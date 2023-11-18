from django.db import models

class product(models.Model):
    item=models.CharField(max_length=50)
    image=models.TextField(max_length=500)
    price=models.CharField(max_length=12)
    def __str__(self):
        return self.item

# Create your models here.
