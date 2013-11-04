from django import forms 
from django.forms import ModelForm 
from models import Service, Subject_type, Resource_type, Action_type

#subject_choices= (
#	('0', 'Identity'), ('1', 'Deparment'),)
#resource_choices= (
#('0', 'Identity'), ('1', 'Deparment'),)
#action_choices= (
#('0', 'Read'), ('1', 'Modify'), ('2', 'Delete') )
#enviroment_choices= (
#	('0', 'Time'), ('1', 'ip_address'),)

class Configure_template(ModelForm):
    class Meta: 
    	model = Service
    	exclude = ("name, customer, serviceprovider")


    #subject_type = forms.ChoiceField(widget=forms.RadioSelect, choices=Subject_type.objects.all())
	#resource_type = forms.ChoiceField(choices=resource_choices)
	#action_type = forms.ChoiceField(choices=action_choices)
	#enviroment_type = forms.ChoiceField(choices=enviroment_choices)




