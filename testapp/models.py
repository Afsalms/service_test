from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)
	map_to_choice = ((0, 'Service Item'),(1, 'BrandModelCategoryMap'),(2, 'Symptom'))
	map_to = models.IntegerField(choices=map_to_choice)

	def __str__(self):
		return self.name


class ServiceItem(models.Model):
	name = models.CharField(max_length=255, unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class BrandModelCategoryMap(models.Model):

	brand_model = models.OneToOneField(ContentType, on_delete=models.CASCADE)
	category = models.OneToOneField(Category, on_delete=models.CASCADE)


class BrandModelServiceItemMap(models.Model):
	brand_model = models.OneToOneField(ContentType, on_delete=models.CASCADE)
	service_item = models.OneToOneField(ServiceItem, on_delete=models.CASCADE)



class Symptom(models.Model):
	text = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	service_item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE, null=True, blank=True)



