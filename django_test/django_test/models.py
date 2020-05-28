from django.db import models

class Restaurant(models.Model):
    res_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    location_numeral = models.CharField(max_length=100)
    webpage = models.CharField(max_length=100)
    price = models.IntegerField()
    menus = models.CharField(max_length=200)
    grade = models.FloatField()
    review1 = models.TextField()
    review2 = models.TextField()
    review3 = models.TextField()