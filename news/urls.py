from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('girl_add/', GirlAddView.as_view(), name='girl_add'),
    path('girls_filter/<str:title>/', girls_filter, name='girls_filter'),
    path('girl_update/<int:girl_id>/', GirlUpdateView.as_view(), name='girl_update'),
    path('girl_delete/<int:girl_id>/', girl_delete, name='girl_delete'),
    path('girl_biography/<int:girl_id>/', girl_biography, name='girl_biography'),
]
