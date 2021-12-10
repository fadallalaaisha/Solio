# from django.urls import path
# from .views import home

# urlpatterns=[
#     path("register/",home, name="home")
# ]

# <int:year>/<str:month>

from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
]