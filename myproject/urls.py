from django.conf.urls import patterns, include, url
from django.contrib import admin
from calendarApp.models import User,Task
 
from rest_framework import routers, serializers, viewsets
from calendarApp.api import TaskList,TaskDetail,UserTaskList,UserDetail,UserList
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

user_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/tasks$', UserTaskList.as_view(), name='usertask-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^/$', UserList.as_view(), name='user-list')
)

task_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', TaskDetail.as_view(), name='task-detail'),
    url(r'^$', TaskList.as_view(), name='task-list'),
)
mycalendar_urls=patterns('',
    url(r'^/login$','calendarApp.views.login'),
    url(r'^/$','calendarApp.views.mycalendar'),
    url(r'^/logout$','calendarApp.views.logout'), 
    url(r'^/register$','calendarApp.views.register'),
    url(r'^/admin/',include(admin.site.urls)),
)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mycalendar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users', include(user_urls)),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(router.urls)),
    #url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tasks', include(task_urls)),
    #url(r'^week/', TemplateView.as_view(template_name='week.html')),
    #url(r'^month/', TemplateView.as_view(template_name='month.html')),
    #url(r'^mycalendar/', TemplateView.as_view(template_name='year.html')),
    url(r'^mycalendar', include(mycalendar_urls)),
)
