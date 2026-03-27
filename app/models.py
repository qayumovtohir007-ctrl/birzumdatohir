from django.db import models

class Contact(models.Model):
    name = models.CharField()
    course = models.CharField(null=True, blank=True)
    phone_number = models.CharField()

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    img = models.ImageField()
    title = models.CharField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField()
    author = models.CharField()

    def __str__(self):
        return self.title




class Product(models.Model):
    img = models.ImageField()
    title = models.CharField()
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    old_price = models.IntegerField(null=True, blank=True)
    created_at = models.DateField()
    author = models.CharField()

    def __str__(self):
        return self.title