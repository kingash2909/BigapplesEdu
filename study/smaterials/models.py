from django.db import models


# Create your models here.


class CourseName(models.Model):
    title2 = models.CharField(max_length=200)
    urlname = models.CharField(max_length=200)

