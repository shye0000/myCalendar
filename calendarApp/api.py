from rest_framework import generics, permissions
from calendarApp.serializers import UserSerializer,TaskSerializer
from calendarApp.models import User,Task
from calendarApp.permissions import TaskAuthorCanEditPermission
#from .permissions import PostAuthorCanEditPermission
class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'    

class TaskMixin(object):
    model = Task
    serializer_class = TaskSerializer
    permission_classes = (TaskAuthorCanEditPermission,)
    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.author = self.request.user
        return super(TaskMixin, self).pre_save(obj)    

class TaskList(TaskMixin, generics.ListCreateAPIView):
    pass

class TaskDetail(TaskMixin, generics.RetrieveUpdateDestroyAPIView):
    model = Task
    serializer_class = TaskSerializer
    def get_queryset(self):
        task_id = self.kwargs['pk']
        return Task.objects.filter(id=task_id)
        #queryset = super(UserTaskList, self).get_queryset()
        #return queryset.filter(author__username=self.kwargs.get('username'))

class UserTaskList(generics.ListAPIView):
    model = Task
    serializer_class = TaskSerializer
    def get_queryset(self):
	username = self.kwargs['username']
        return Task.objects.filter(author__username=username)
	#queryset = super(UserTaskList, self).get_queryset()
        #return queryset.filter(author__username=self.kwargs.get('username'))    
