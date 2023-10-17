from django.db import models


# Create your models here.
# product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
