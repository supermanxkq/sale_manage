from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
# 产品类型表
class GoodsType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(default='', max_length=500)
    code = models.CharField(max_length=10, unique=True, default='')





class User(AbstractUser):
    img = models.ImageField(upload_to='img',default='')
    phone =models.CharField(max_length=11,unique=True,default='')
    birthday=models.DateField(auto_now_add=True)
    interests=models.CharField(default='',max_length=100)
    address=models.CharField(default='',max_length=100)








