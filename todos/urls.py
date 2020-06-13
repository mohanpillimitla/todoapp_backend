
from django.urls import path,include
from .views import TodoView

from rest_framework import routers                  

router = routers.DefaultRouter()                      # add this
router.register(r'todos',TodoView, 'todo')   







urlpatterns = [

            path('', include(router.urls))               
]
