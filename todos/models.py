from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=128)
    project_details = models.TextField(null=True, blank=True)
    # tasks = models.ForeignKey(to=Task, on_delete=models.CASCADE,null=True)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_name
    def get_absolute_url(self):
        return reverse("proj_details", kwargs={"pk": self.pk})
    
class Task(models.Model):
    task_name = models.CharField(max_length=256)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='project_tasks', related_query_name='project_tasks')
    task_details = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField()
    time_taken = models.DurationField(null=True,)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name
    
