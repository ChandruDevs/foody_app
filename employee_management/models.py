from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    team_id = models.ForeignKey("Team", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    team_lead_id = models.ForeignKey("Employee", on_delete=models.SET_NULL, null=True)
