import re
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task


# Create your views here.
def index(request):
    to_do_items = Task.objects.all().order_by("added_time")
    return render(request, 'To_Do/index.html', {"to_do_items": to_do_items})


def add_task(request):
    added_date = timezone.now()
    content = request.POST['content']
    created_obj = Task.objects.create(added_time=added_date, task_to_do=content)
    return HttpResponseRedirect('/')