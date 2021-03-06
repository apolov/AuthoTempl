from django.contrib import admin
from login.models import Service, Subject_type, Resource_type, Action_type, Enviroment_type
from databasec1.models import Deparment, Employee


class ServiceAdmin(admin.ModelAdmin):
	filter_horizontal = ('serviceprovider', 'customer',)

admin.site.register (Service, ServiceAdmin)
# admin.site.register (Service_provider)
admin.site.register (Subject_type)
admin.site.register (Resource_type)
admin.site.register (Action_type)
admin.site.register (Enviroment_type)
# admin.site.register (Customer)
admin.site.register (Deparment)
admin.site.register (Employee)