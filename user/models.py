from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateField()
    updated_at=models.DateField(null=True, blank=True)
    