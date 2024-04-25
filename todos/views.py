from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.


@login_required(login_url='/login')
def index(request, ):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'projects':projects,
        'tasks': tasks,
    }
    return render(request, 'todos/project_list.html', context)

