from django.db import models

# Create your models here.
class Store(models.Model):
    app=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    rating=models.DecimalField(max_digits=5, decimal_places=2,)
    def __str__(self):
        return self.app
