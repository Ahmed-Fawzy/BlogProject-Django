from django.db import models
from  django.utils.timezone import datetime
# Create your models here.



class Permission(models.Model):

    permi_type = models.CharField(max_length=50,unique=True)

#    user = models.ManyToManyField(User)

    def __str__(self):
        return self.permi_type


class User(models.Model):

    user_name = models.CharField(max_length=255, unique=True)
    user_email = models.EmailField(max_length=255, unique=True, null=True)
    user_pass = models.CharField(max_length=50, default='')

    permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.user_name


class Post(models.Model):

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    published = models.BooleanField(choices=BOOL_CHOICES, default=False)
    recommended = models.BooleanField(choices=BOOL_CHOICES, default=False)


    def __str__(self):
        return self.title

#class Manage(models.Model):

#    user = models.ManyToManyField(User,unique=True)

#    permit = models.ManyToManyField(Permission)

#    def __str__(self):
#        return self.user
