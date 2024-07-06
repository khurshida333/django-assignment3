from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
        else:
            return render(request, 'add_task.html', {'task_form': task_form})
    else:
        task_form = forms.TaskForm()
        return render(request, 'add_task.html',{'task_form': task_form})
    
    
def complete_task(request,task_id):
    task = models.Task.objects.get(id=task_id)
    task.Is_Completed=True
    task.save()
    return redirect('show_task')

def edit_task(request,id):
    task = models.Task.objects.get(pk=id)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm(instance=task)
    return render(request, 'add_task.html',{'task_form': task_form})
    
def delete_task(request,id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
