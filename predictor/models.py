from django.db import models

# Create your models here.

class AdvertisementCategory(models.Model):
    categoryName=models.CharField(max_length=200)
    def __str__(self):
        return self.categoryName


class Advertisement(models.Model):
    adName = models.CharField(max_length=200)
    adContent = models.TextField(max_length=200)
    categoryName=models.ForeignKey(AdvertisementCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.adName

class objectCategory(models.Model):
    object=models.CharField(max_length=200)
    categoryName=models.ForeignKey(AdvertisementCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.object