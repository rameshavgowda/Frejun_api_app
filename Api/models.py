from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

status_choices=(
    ('Assigned','Assigned'),
    ('Under review','Under review'),
    ('Progress','Progress'),
    ('Done','Done')
)
team_choice=(
    ('Developer','Developer'),
    ('Tester','Tester'),
    ('Busness analyst','Busness analyst'),
    ('Technical lead','Technical lead')
)

class CustomeUser(models.Model):
    Team = models.CharField(max_length=100, choices=team_choice)
    Team_Leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'admin')
    Team_Member = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user')
    class Meta:
        abstract = True

class Team(CustomeUser):
    Name = models.CharField(max_length=100)
    Team = None

    def __str__(self):
        return str(self.Team_Member)

    # def Team_members(self):
    #     return ",".join([str(p) for p in self.Team_Member.all()])

class Task(CustomeUser):
    Team_Member = models.ForeignKey(Team, on_delete= models.CASCADE)
    Status = models.CharField(max_length=100, choices=status_choices, default=1)
    Started_at = models.DateField()
    Completed_at = models.DateField()
    Team_Leader= None

    # def __str__(self):
    #     return self.Team_Member


