from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
   writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
   title = models.CharField(max_length=20, null=True)
   image = models.ImageField(upload_to='project/', null=False)
   description = models.CharField(max_length=200,null=True)

   created_at = models.DateField(auto_now_add=True, null=True)

   #article create 진행할 때 project 선택 창에 project 이름이 드러나도록 구현
   def __str__(self):
      return f'{self.pk} : {self.title}'
