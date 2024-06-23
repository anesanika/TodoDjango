from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class TasksModel(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  IsDone = models.BooleanField(default=False)
  user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

  def __str__(self):
    return self.title
