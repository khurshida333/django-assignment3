from django.db import models
from categories.models import Category
# Create your models here.

class Task(models.Model):
    Task_Title = models.CharField(max_length=50)
    Task_Description = models.TextField()
    Is_Completed = models.BooleanField(default=False)
    Task_Assign_Date =models.DateField()
    category =models.ManyToManyField(Category)

    
    def __str__(self):
        return f'Task - {self.Task_Title}'
