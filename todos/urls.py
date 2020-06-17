
from django.urls import path,include
from .views import TodoView,MovieView

from rest_framework import routers                  

router = routers.DefaultRouter()                      # add this
router.register(r'todos',TodoView, 'todo')   
router.register(r'movies',MovieView, 'movie')   








urlpatterns = [

            path('', include(router.urls))               
]
