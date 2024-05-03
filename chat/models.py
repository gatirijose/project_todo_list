from django.db import models
from django.contrib.auth.views import UserModel
from django_quill.fields import QuillField
from todos.models import Project

# Create your models here.

# class Chat(models.Model):
#     subject = models.ForeignKey(Project, on_delete=models.CASCADE)
#     messages = models.ManyToManyField('chat.message')


class Message(models.Model):
    subject = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    message = QuillField(null=True)