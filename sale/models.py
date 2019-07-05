from django.db import models
from django.contrib.auth.models import AbstractUser

# 产品类型表
class GoodsType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(default='', max_length=500)
    code = models.CharField(max_length=10, unique=True, default='')





class User(AbstractUser):
    img = models.ImageField(upload_to='img',default='')












