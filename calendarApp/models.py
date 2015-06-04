from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)
class Task(models.Model):
	author = models.ForeignKey(User, related_name='tasks')
	taskTitle = models.CharField(max_length=200)
	color=models.CharField(max_length=200,default='#FAD165')
	taskDetail = models.TextField()
	dateStart = models.DateField()
	dateEnd = models.DateField()
	timeStart = models.TimeField()
	timeEnd = models.TimeField()
	def __unicode__(self):
		return u'%s %s' % (self.author.username, self.taskTitle)