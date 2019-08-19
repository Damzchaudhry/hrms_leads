from django.db import models

from django.db import models
import math 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from Jobs.models import Jobs

job_choice=(
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
   
 )

class Candidate(models.Model):
	Job_id = models.OneToOneField(Jobs, on_delete=models.CASCADE, null=True)
	Name = models.CharField(max_length=100,verbose_name="Name")
	Email = models.CharField(max_length=100,verbose_name='Email')
	Contact = models.CharField(max_length=10,verbose_name='Contact')
	Exp = models.CharField(max_length=100,verbose_name='Exp')
	apply_Date=models.DateTimeField(auto_now_add=True,verbose_name="apply_Date")



	def __str__(self):
		return self.Name
	


		

