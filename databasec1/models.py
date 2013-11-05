from django.db import models

class Deparment(models.Model):
	name=models.CharField(max_length=140);

	def __unicode__(self):
		return self.name 

class Employee(models.Model):
	name = models.CharField(max_length=140);

	def __unicode__(self):
		return self.name 

# Create your models here.
