from django.urls import path

from . import views

urlpatterns = [
     path('', views.ListTodo.as_view(), name='list_todo'),
    path('<int:pk>', views.DetailTodo.as_view(), name='todo_detail'),
]