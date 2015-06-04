from django.shortcuts import render_to_response,render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from calendarApp.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from calendarApp.forms import LoginForm,RegisterForm
def mycalendar(request):
	if request.user.is_authenticated():
		return render_to_response('year.html', RequestContext(request, {'user': request.user}))
	else:
		return redirect('/mycalendar/login')
def logout(request):
    auth.logout(request)
    form = LoginForm()
    return redirect('/mycalendar/login')

def login(request):
	if request.user.is_authenticated():
		return redirect('/mycalendar/')
	else:		
		if request.method == 'GET':
			auth.logout(request)
			form = LoginForm()
			return render_to_response('login.html', RequestContext(request, {'form': form,}))
		else:
			
			form = LoginForm(request.POST)
			if form.is_valid():
				#auth.logout(request)
				username = request.POST.get('username', '')
				password = request.POST.get('password', '')
				user = auth.authenticate(username=username, password=password)
				
				if user is not None and user.is_active:
					auth.login(request, user)
					return redirect('/mycalendar/')
				else:
					return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
			else:
				return render_to_response('login.html', RequestContext(request, {'form': form,}))  
def register(request):
	if request.method == 'GET':
		form = RegisterForm()
		return render_to_response('register.html', RequestContext(request, {'form': form,}))
	else:
		form = RegisterForm(request.POST)
		loginForm=LoginForm()
		if form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			password2 = request.POST.get('password2', '')
			email = request.POST.get('email', '')
			firstname=request.POST.get('firstname', '')
			lastname=request.POST.get('lastname', '')
			if password==password2:
				user = User.objects.create_user(username, email, password)
				user.first_name=firstname
				user.last_name=lastname
				user.save()
				return redirect('/mycalendar/login')
			else:
				return render_to_response('register.html', RequestContext(request, {'form': form,'password_is_wrong':True}))	
		else:
			return render_to_response('register.html', RequestContext(request, {'form': form,}))  
