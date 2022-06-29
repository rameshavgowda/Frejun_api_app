from rest_framework import serializers
from .models import Team,Task

class TaskSerializer(serializers.ModelSerializer):
   class Meta:
       model=Task
       fields=['id','Team','Team_Member','Status','Started_at','Completed_at']

class TeamSerializer(serializers.ModelSerializer):
    #Team_members=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
       model=Team
       fields= '__all__'

class TaskstatusSerializer(serializers.ModelSerializer):
   class Meta:
       model=Task
       fields=['id','Team','Team_Member','Status','Started_at','Completed_at']
       read_only_fields = ['id','Team','Team_Member','Started_at','Completed_at']