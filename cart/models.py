from django.db import models
import django.utils.timezone as timezone
from goods.models import Goods
from sale.models import User
from decimal import Decimal


# 供应商表
class Cart(models.Model):
    goods_id = models.ForeignKey(Goods,related_name="cart_goods_id",on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)
    cr_us_id=models.ForeignKey(User,related_name="cart_user_id",on_delete=models.CASCADE)
    num=models.IntegerField(default=0)
    goods_name=models.CharField(default='',max_length=50)
    sale_price=models.DecimalField(max_digits=10,decimal_places=2)


