from calendarApp.models import User

class AlwaysAdminBackend(object):
    def authenticate(self, *args, **kwargs):
    	"""Always returns the `admin` user.  DO NOT USE THIS IN PRODUCTION!"""
    	return User.objects.get(username='admin')

    def get_user(self, user_id):
    	return User.objects.get(username='admin')