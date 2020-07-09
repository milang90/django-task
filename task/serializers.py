from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "content", "status") # new
        model = Task
