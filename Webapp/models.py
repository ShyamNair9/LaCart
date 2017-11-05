from django.db import models

# Create your models here.
class Fridge(models.Model):
	name = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class ShoppingCart(models.Model):
	item = models.CharField(max_length=500)
	quantity = models.IntegerField()
	unit = models.CharField(max_length = 10)
	


