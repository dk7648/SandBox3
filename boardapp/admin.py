from django.contrib import admin

# Register your models here.

from boardapp.models import Board
from commentapp.models import Comment

admin.site.register(Board)
admin.site.register(Comment)
