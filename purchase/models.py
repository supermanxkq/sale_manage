from django.db import models
import django.utils.timezone as timezone
from goods.models import Goods
from sale.models import User
from decimal import Decimal


class Purchase(models.Model):
    goods_id = models.ForeignKey(Goods, related_name='purchase_goods_id', on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=20)
    num = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    single_price = models.DecimalField(decimal_places=2, max_digits=10)
    create_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20)


