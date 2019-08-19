from django.db import models
import math 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.utils.timesince import timesince



class Dept(models.Model):
	name=models.CharField(max_length=50,verbose_name="name")

	def __str__(self):
		return self.name

class Job_type(models.Model):
	name=models.CharField(max_length=50,verbose_name="name")
	def __str__(self):
		return self.name


class Status(models.Model):
	name=models.CharField(max_length=50,verbose_name="name")
	def __str__(self):
		return self.name


class Jobs(models.Model):
	title = models.CharField(max_length=100,verbose_name='title')
	dept = models.ForeignKey(Dept,on_delete = models.CASCADE,verbose_name = "dept",related_name="jobs")
	job_location = models.CharField(max_length=100,verbose_name='job_location')
	vacancy = models.CharField(max_length=10,verbose_name='vacancy')
	exp = models.CharField(max_length=100,verbose_name='exp')


	salary_from =models.CharField(max_length=100,verbose_name='salary_from')
	salary_to=models.CharField(max_length=100,verbose_name='salary_to')
	job_type = models.ForeignKey(Job_type,on_delete = models.CASCADE,verbose_name = "job_type",related_name="jobs")
	status = models.ForeignKey(Status,on_delete = models.CASCADE,verbose_name = "status",related_name="jobs")

	start_date = models.DateTimeField(auto_now_add=True,verbose_name="start_date")
	end_date = models.DateField(default='2020-07-01',verbose_name='end_date')
	updated_date = models.DateTimeField(auto_now=True)

	desc = models.CharField(max_length=1500,verbose_name='desc')

	skill=models.CharField(max_length=5000,verbose_name='skill')
	email=models.CharField(max_length=55,verbose_name="email")
	contact=models.CharField(max_length=15,verbose_name="contact")




	def __str__(self):
		return self.title

	def __str__(self):
		return self.dept
	def Time_dif():
		t1=date.today()
		t2=end_date
		end_in=Time_left.days
		return timesince(t1 ,t2)



		
