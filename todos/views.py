from django.shortcuts import render

# Create your views here.

from .models import TodoModel,MovieModel

    


from .serializers import TodoSerializer



from rest_framework import viewsets,generics



 

class TodoView(viewsets.ModelViewSet):       # add this
      serializer_class = TodoSerializer          # add this
      queryset = TodoModel.objects.all()  


class MovieView(viewsets.ModelViewSet):       # add this
      serializer_class = TodoSerializer          # add this
      queryset = MovieModel.objects.all()  


