from django.db import models


class Job(models.Model):
    image_s = models.ImageField(upload_to='imgaes/')
    summary = models.CharField(max_length=200)