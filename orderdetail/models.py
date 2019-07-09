from django.db import models
import django.utils.timezone as timezone
from sale.models import GoodsType
from goods.models import Goods
from merchant.models import Merchant
from order.models import Order


# 订单详情表
class OrderDetail(models.Model):
    merchant_id = models.ForeignKey(Merchant, related_name='order_detail_mer_id', on_delete=models.CASCADE)
    goods_id = models.ForeignKey(Goods, related_name='order_detail_goods_id', on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=20)
    num = models.IntegerField()
    sale_price = models.DecimalField(decimal_places=2, max_digits=10)
    goodsType_id = models.ForeignKey(GoodsType, related_name='order_detail_goods_type_id', on_delete=models.CASCADE)
    goodsType_Name = models.CharField(max_length=20, default='')
    order_id = models.ForeignKey(Order,max_length=50, related_name='order_detail_order_id', to_field='order_code', on_delete=models.CASCADE)
