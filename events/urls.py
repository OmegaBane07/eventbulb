from . import views
from django.urls import path

urlpatterns= [
    path('<int:id>/', views.details, name='events_details'),
    path('', views.list, name='events_list'),
    path('<int:id>/add_attending/',views.add_attending, name="events_add_attending"),
    path('<int:id>/remove_attending/',views.remove_attending, name="events_remove_attending"),
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('<int:id>/review/new', views.new_review ,name='new_review'),

]