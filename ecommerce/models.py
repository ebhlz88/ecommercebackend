from django.db import models

# Create your models here.
class product(models.Model):
    productname = models.CharField(max_length=50)
    productdisc = models.CharField(max_length=50)
    product_photo = models.ImageField(upload_to='productimage')