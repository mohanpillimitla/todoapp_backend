from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class TodoModel(models.Model):

	title=models.CharField(max_length=200)
	
	iscompleted=models.BooleanField()


class MovieModel(models.Model):

	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	genre=models.CharField(max_length=20)
	stock=models.IntegerField()
	rate=models.IntegerField()
	like=models.BooleanField()