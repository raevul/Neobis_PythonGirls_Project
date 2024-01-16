from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create_new/', NewCreateView.as_view(), name='create_new'),
    path('update_new/<int:new_id>/', NewUpdateView.as_view(), name='update_new'),
    path('delete_new/', NewDeleteView.as_view(), name='delete_new'),
    path('new_detail/<int:new_id>/', new_detail, name='new_detail'),
]
