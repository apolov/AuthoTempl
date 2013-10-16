from django.contrib import admin
from login.models import Service, Subject_type, Resource_type, Action_type, Enviroment_type


class ServiceAdmin(admin.ModelAdmin):
	filter_horizontal = ('serviceprovider',)

admin.site.register (Service, ServiceAdmin)
admin.site.register (Subject_type)
admin.site.register (Resource_type)
admin.site.register (Action_type)
admin.site.register (Enviroment_type)