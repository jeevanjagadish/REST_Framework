from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    phoneno = models.IntegerField()

class Company(models.Model):
    company_name = models.CharField(max_length=10)
    address =  models.CharField(max_length=100)
    phoneno = models.IntegerField()
    Technology = models.CharField(max_length=100)
    company_size = models.IntegerField()
    company_ceo = models.CharField(max_length=20)


