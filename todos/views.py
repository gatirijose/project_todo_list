from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, UserModel
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


@login_required(login_url='/login')
def index(request, ):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'projects':projects,
        'tasks': tasks,
    }
    return render(request, 'todos/project_list.html', context)

@login_required(login_url='/login')
def project_details(request, proj_num):
    project = get_object_or_404(Project, pk=proj_num)
    tasks = Task.objects.all()
    context = {
        'project':project,
        'tasks': tasks,
    }
    return render(request, 'todos/project_details.html', context)

class UserCreateView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'todos/registration/sign-up.html'
    success_url = '/'
