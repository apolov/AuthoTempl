from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,  BaseUserManager
from django.forms import ModelForm

class Subject_type(models.Model):
	name = models.CharField(max_length=140);
	
	def __unicode__(self):
		return self.name 

class Resource_type(models.Model):
	name = models.CharField(max_length=140);
	
	def __unicode__(self):
		return self.name 

class Action_type(models.Model):
	name = models.CharField(max_length=140);
	
	def __unicode__(self):
			return self.name

class Enviroment_type(models.Model):
	name = models.CharField(max_length=140);
	
	def __unicode__(self):
			return self.name 


# class Service_provider(models.Model):
# 	company = models.CharField(max_length=140);

# 	def __unicode__(self):
# 			return self.company

# class Customer(BaseUser):
# 	name = models.CharField(max_length=140);

# 	def __unicode__(self):
# 			return self.name
	
class Service(models.Model):
	name = models.CharField(max_length=140)
	subject_class = models.ForeignKey(Subject_type)
	resource_class = models.ForeignKey(Resource_type)
	action_class = models.ForeignKey(Action_type)
	enviroment_class = models.ForeignKey(Enviroment_type)
	serviceprovider = models.ManyToManyField(User, related_name="Serviceprovider")   
	customer= models.ManyToManyField(User, related_name="Customer")

	def __unicode__(self):
			return self.name 