from django.db import models
from django.contrib.auth.models import User 
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

#class Subject_typeForm(ModelForm):
 #   class Meta:
  #      model = Subject_type
   #     fields = ['name']

class Service(models.Model):
	name = models.CharField(max_length=140)
	subject_class = models.OneToOneField(Subject_type)
	resource_class = models.OneToOneField(Resource_type)
	action_class = models.OneToOneField(Action_type)
	enviroment_class = models.OneToOneField(Enviroment_type)
	serviceprovider = models.ManyToManyField(User)   

	def __unicode__(self):
			return self.name 



#class Membership(models.Model):
    #service = models.ForeignKey(Service)
    #user = models.ForeignKey(User)
    #invite_reason = models.CharField(max_length=64)


# Create your models here.
