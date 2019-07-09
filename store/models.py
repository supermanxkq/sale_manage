from django.db import models
import django.utils.timezone as timezone

from goods.models import Goods
# 仓库表
class Store(models.Model):
    goods_id = models.ForeignKey(Goods, related_name='store_goods_id', on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=20)
    num = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    single_price = models.DecimalField(decimal_places=2, max_digits=10)
    create_time = models.DateTimeField(default=timezone.now)
