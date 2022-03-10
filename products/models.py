from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at=models.DateField()
    updated_at=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name