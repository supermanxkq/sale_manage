from django.db import models
import django.utils.timezone as timezone
from goods.models import Goods

# 信息表
class Msg(models.Model):
    # 信息名称
    name = models.CharField(max_length=10)
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now)
    # 信息级别
    level = models.CharField(max_length=10, default='')
    #数量
    num = models.IntegerField(default=0)
    # 商品名称
    goods_name=models.CharField(max_length=100,default='')
    # 商品ID
    goods_id = models.ForeignKey(Goods, related_name='msg_goods_id', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

