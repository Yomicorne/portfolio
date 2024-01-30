from django.db import models

# Create your models here.
from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Applicant(models.Model):
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    # Add other fields according to the applicant details

class Application(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='new')
    # Add other fields like resume, cover letter, etc.
