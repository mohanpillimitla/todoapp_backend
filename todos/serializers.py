from rest_framework import serializers
from .models import TodoModel,MovieModel


class TodoSerializer(serializers.ModelSerializer):

	class Meta:
		model=TodoModel
		fields = ('id', 'title', 'iscompleted')


class MovieSerializer(serializers.ModelSerializer):

	class Meta:
		model=MovieModel
		fields = ('__all__')
		read_only_field='user'


