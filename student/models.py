from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length=40)
    stud_class = models.TextField()
    department = models.TextField()
    score = models.IntegerField()
    image_url = models.CharField(max_length=2048)
    

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.FloatField()
#     stock = models.IntegerField()
#     image_url = models.CharField(max_length=2048)
