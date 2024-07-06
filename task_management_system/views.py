from django.shortcuts import render
from tasks.models import Task
# Create your views here.


def showTask(request):
    data = Task.objects.all()
    return render(request, 'home.html',{'data': data})