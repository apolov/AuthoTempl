from django.contrib import admin
from login.models import Service


class ServiceAdmin(admin.ModelAdmin):
	filter_horizontal = ('serviceprovider',)

admin.site.register(Service, ServiceAdmin) 