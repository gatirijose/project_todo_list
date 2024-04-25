from django.contrib import admin
from .models import *
# Register your models here.

# Task
# ProjectTasks
# admin.site.register(Task)

class TaskInine(admin.StackedInline):
    model = Task
    extra=1


@admin.register(Project)
class ProjectTasksAdmin(admin.ModelAdmin):
    inlines = [
        TaskInine,
    ]

    # pass
    
# admin.site.register(Task)