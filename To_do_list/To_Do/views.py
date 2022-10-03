from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
# Create your views here.
def index(request):
    task_obj = Task.objects.all()
    print(task_obj.task_to_do)
    return render(request, 'To_Do/index.html')