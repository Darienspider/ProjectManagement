from django.db import models
import datetime
# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)  # Using CharField is more efficient for this.
    description = models.TextField(max_length=1000)
    start_dt = models.DateTimeField(null=True, blank=True)  # Add blank=True to allow empty start date
    end_dt = models.DateTimeField(null=True, blank=True)  # Same for end date
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the time when the project is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update the time when the project is updated
    
    # Optionally add priority, budget, and client if needed
    priority = models.IntegerField(default=0)  # Example: Can define low, medium, high priority
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Budget for the project


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, verbose_name=("Project Task"), on_delete=models.CASCADE)
    title = models.TextField(max_length= 1000)
    description = models.TextField(max_length=1000)
    status = models.CharField(choices=[
            ('pending','Pending'),
            ('in progress', 'In Progress'),
             ('completed','Completed')
            ]
            , max_length= 20
    )

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    industry = models.CharField(max_length=1000, null=True, blank=True)  # e.g., 'Technology', 'Construction'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.TextField(max_length=1000)
    lastName = models.TextField(max_length=1000)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)