from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=255)
	url = models.TextField()
	pub_date = models.DateTimeField(default=datetime.now)
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def summary(self):
		return self.body[:100]

	def __str__(self):
		return self.title
