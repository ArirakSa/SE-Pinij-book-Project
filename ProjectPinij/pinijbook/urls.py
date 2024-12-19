from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('signin/', sign_in, name='signin'),
    path('signup/', sign_up, name='signup'),
]