from django.contrib import admin
from .models import Message
# Register your models here.

# class MessageInline(admin.StackedInline):
#     model = Message
#     extra = 3


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass