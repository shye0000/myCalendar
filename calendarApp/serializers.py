from rest_framework import serializers
from calendarApp.models import User,Task
class UserSerializer(serializers.ModelSerializer):
	tasks = serializers.HyperlinkedIdentityField(view_name='usertask-list',lookup_field='username')
	class Meta:
	 	model = User
	 	fields = ('id', 'username', 'first_name', 'last_name', 'tasks', )
class TaskSerializer(serializers.ModelSerializer):
	author = UserSerializer(required=False)
	def get_validation_exclusions(self, *args, **kwargs):
	# Need to exclude `user` since we'll add that later based off the request
		exclusions = super(TaskSerializer, self).get_validation_exclusions(*args, **kwargs)
		return exclusions + ['author']
	class Meta:
		model = Task
