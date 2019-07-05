from django.db import models
import django.utils.timezone as timezone

# 供应商表
class Merchant(models.Model):
    name = models.CharField(max_length=10)
    create_time = models.DateTimeField(default=timezone.now)
    where_from = models.CharField(max_length=10, default='')
    mark = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号', default='')
    address = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name

