
from . import views
from django.urls import path

urlpatterns = [
    path('',views.signup,name='signup'),
    path('loginn',views.loginn,name='loginn'),
    path('index',views.index,name='index')
]
