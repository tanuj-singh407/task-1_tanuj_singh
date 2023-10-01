from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('url/task/', views.task_page, name='task_page'),
]