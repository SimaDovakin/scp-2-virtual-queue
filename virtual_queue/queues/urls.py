from django.urls import path

from . import views


app_name = 'queues'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create_queue', views.create_queue, name='create_queue'),
    path('delete_queue/<int:queue_id>', views.delete_queue, name='delete_queue')
]
