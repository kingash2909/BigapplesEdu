from django.db import models
from datetime import datetime


# Create your models here.


class Course_Details(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=500)
    expiry_date = models.TextField(max_length=200)
    updated_date = models.DateTimeField(default=datetime.now())
    stitle = models.CharField(max_length=200)
    buttonText = models.URLField(max_length=500)
    price = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title
