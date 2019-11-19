from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
def set_deleted_user():
    User = get_user_model()
    return User.objects.get_or_create(username='deleted')[0]

class Car(models.Model):
    car = models.CharField(max_length= 100)
    user = models.ForeignKey(User,on_delete=models.SET(set_deleted_user))

    def __str__(self):
        return self.car