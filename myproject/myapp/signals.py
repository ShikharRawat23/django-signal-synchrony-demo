import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=Student)
def after_student_save(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(5) 
    print("Signal finished!")
