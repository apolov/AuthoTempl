from django.db import models
from django.contrib.auth.models import User 


class Service(models.Model):
	name = models.CharField(max_length=140)
	serviceprovider = models.ManyToManyField(User)   

	def __unicode__(self):
		return self.name 

#class Membership(models.Model):
    #service = models.ForeignKey(Service)
    #user = models.ForeignKey(User)
    #invite_reason = models.CharField(max_length=64)


# Create your models here.
