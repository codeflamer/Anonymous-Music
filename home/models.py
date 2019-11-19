from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True)
    post = models.CharField(max_length=360)


class Friends(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, related_name='owner')
    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls,current_user,new_friend):
         friend,created=cls.objects.get_or_create(
             current_user=current_user
         )
         friend.users.remove(new_friend)
    class Meta:
        verbose_name_plural='Friends'

class Tweet(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date=models.DateTimeField(auto_now=True,auto_now_add=False)




