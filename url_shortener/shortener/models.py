from django.db import models

# Create your models here.
class URL(models.Model):
	long_url = models.TextField()