from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Login(AbstractUser):
    userType = models.CharField(max_length=100)
    viewPass = models.CharField(max_length=100)


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)


class Questions(models.Model):
    uid = models.ForeignKey(Registration, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)


class Answers(models.Model):
    qid = models.ForeignKey(Questions, on_delete=models.CASCADE)
    uid = models.ForeignKey(Registration, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
