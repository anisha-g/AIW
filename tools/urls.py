from django.urls import path
from tools import views

urlpatterns = [
    path("",views.home,name='home'),
]
 