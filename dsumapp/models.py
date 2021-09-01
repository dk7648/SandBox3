import re

from ckeditor.fields import RichTextField
import ckeditor
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Dsum(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='dsum', null=True)
    title = models.CharField(max_length=200, null=True)
    content = RichTextField(null=True)


    created_at = models.DateField(auto_now_add=True, null=True)

    def summary(self):
        return self.content[:200]

    def temp(self):
        remove_tags = re.compile('<.*?>')
        return re.sub(remove_tags, '', self.content)