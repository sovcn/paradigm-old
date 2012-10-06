from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
import math


class UserProfile(models.Model):
    
    
    user = models.OneToOneField(User)
    
    displayName = models.CharField(max_length=30,null=True,blank=True)

    
    def __unicode__(self):
        return str(self.displayName)
    
    def updateFromProfile(self,profile):
        self.displayName = profile.displayName
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)