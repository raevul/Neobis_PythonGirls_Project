from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create_new/', create_new, name='create_new'),
    path('new_detail/<int:new_id>/', new_detail, name='new_detail'),
]
