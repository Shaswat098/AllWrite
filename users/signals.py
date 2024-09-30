from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# this function allows you to create a profile every time a user is created(signs up)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

# this function saves profile after every profile is created

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()