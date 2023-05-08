from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import * 
from . import serializers

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer