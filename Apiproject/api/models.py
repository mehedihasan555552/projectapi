from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    job = models.ForeignKey('Job',null=True,on_delete = models.SET_NULL)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    passwrod = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    how_many_jobs = models.CharField(max_length=200,null=True,blank=True)
    stars_value = models.CharField(max_length=200,null=True,blank=True)
    distance_in_miles = models.CharField(max_length=200,null=True,blank=True)
    specializes = models.CharField(max_length=200,null=True,blank=True)
    last_reviews = models.CharField(max_length=200,null=True,blank=True)
    profile_picture = models.ImageField(default='default.jpg',max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.name




class Job(models.Model):
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pay = models.CharField(max_length=200)
    job_price = models.CharField(max_length=200,null=True,blank=True)
    job_hours = models.CharField(max_length=200,null=True,blank=True)
    job_type = models.CharField(max_length=200,null=True,blank=True)
    job_media = models.ImageField(default='default.jpg',null=True,blank=True)


    def __str__(self):
        return self.description



class Order(models.Model):
	job = models.ForeignKey(Job, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.job.description
