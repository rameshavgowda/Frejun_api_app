from django.contrib import admin
from .models import Task, Team

# Register your models here.

#admin.site.register(Task)
#admin.site.register(Team)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display= ['id','Team','Team_Member','Status','Started_at','Completed_at']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','Team_Member','Name','Team_Leader']