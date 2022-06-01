from dataclasses import field
from django.db import models


# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='imgaes/')
