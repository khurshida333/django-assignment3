from django import forms
from .import models

class TaskForm(forms.ModelForm):
    class Meta :
        model = models.Task
        fields = ['Task_Title','Task_Description','Is_Completed','Task_Assign_Date','category']
        widgets = {
            'Task_Assign_Date': forms.DateInput(attrs={'type': 'date'}),
        }
