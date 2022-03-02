from . import views
from django.urls import path

urlpatterns= [
    path('details/', views.details, name='events_details'),
    path('', views.list, name='events_list')
]