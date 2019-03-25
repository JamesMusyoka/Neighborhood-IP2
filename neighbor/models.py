from django.db import models
from django.contrib.auth.models import User
import datetime as dt

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=50)
    neighborhood_location = models.CharField(max_length=50, null=True)
    occupants = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True)
    health_dept = models.IntegerField(default='999')
    police_dept = models.IntegerField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.neighborhood_name

    def save_neighborhood(self):
        self.save()

    def create_neighborhood(self):
        self.save

    def find_neighborhood(self):
        self.save

    def update_neighborhood(self):
        self.save

    def update_occupands(self):
        self.save

    def delete_neighborhood(self):
        self.save

    class Meta:
        ordering = ['neighborhood_name']



class User_profile(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    neighborhood = models.ForeignKey(Neighborhood)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank=True)


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(User,null=True,blank=True)
    neighborhood_id = models.ForeignKey(Neighborhood,null=True,blank=True)
    business_email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank=True)


    def save_business(self):
        self.save()

    def  create_business(self):
        self.save()

