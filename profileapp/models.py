from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    #profile과 user객체를 1:1로 연결, on_delete:Profile과 연결된 User객체가없어질 때 행동, profile도 없어짐, 연관짓기 #request.user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #media root 밑에 profile에 저장됨.
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

