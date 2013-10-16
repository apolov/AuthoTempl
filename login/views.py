# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect 
from django.template.context import RequestContext
from django.contrib import auth 
from django.template.loader import get_template
from django.template import Context
from django.core.context_processors import csrf 
from models import Service, Subject_type
from forms import Configure_template


def welcome(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('welcome.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin/')
	else:

		return HttpResponseRedirect('/invalid/')

def loggedin(request):
	service = Service.objects.filter(serviceprovider = request.user) 
	return render_to_response('MedicalServices.html', {'full_name':request.user.username, 'services':service})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

from .serializer import ServiceSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer  

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

def ctemplate(request,id_service):
	services = Service.objects.all()
	#ser = get_object_or_404(Service,pk = id_service)
	ser = Service.objects.get(pk = id_service)
        subject_class = Subject_type.objects.filter(service = ser) 
        full_name = request.user.username
	
        if request.method == 'POST':
            form = Configure_template(request.POST)
            if form.is_valid():
                service = form.save(commit = False)
                service.serviceprovider = request.user
                service.save()
                return HttpResponseRedirect('/loggedin/')
        else:
            form = Configure_template()
        template = "configure_template.html"

        return render_to_response(template,context_instance=RequestContext(request, locals()))


    #form = Configure_template()
    #return render_to_response('configure_template.html',{'form': form})
