from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):

    #profile과 user객체를 1:1로 연결, on_delete:Profile과 연결된 User객체가없어질 때 행동, profile도 없어짐, 연관짓기 #request.user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    #media root 밑에 profile에 저장됨.
    name = models.CharField(max_length=20, null=True)
    number = models.CharField(max_length=10, null=True)

    message = models.CharField(max_length=100, null=True)
