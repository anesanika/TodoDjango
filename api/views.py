from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import TasksModel

# Create your views here.
class TodoViews(viewsets.ModelViewSet):
  queryset = TasksModel.objects.all()
  serializer_class = TaskSerializer
  
  def get_queryset(self):
    return TasksModel.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)