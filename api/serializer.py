from rest_framework import serializers
from .models import TasksModel

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = TasksModel
    fields = ('id', 'title', 'description', 'IsDone', 'user_id')