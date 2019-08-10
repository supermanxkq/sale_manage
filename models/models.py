from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser
from system.storage import ImageStorage


# 产品类型表
class GoodsType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(default='', max_length=500)
    code = models.CharField(max_length=10, unique=True, default='')


class User(AbstractUser):
    img = models.ImageField(upload_to='img', default='')
    phone = models.CharField(max_length=11, unique=True, default='')
    birthday = models.DateField(auto_now_add=True)
    interests = models.CharField(default='', max_length=100)
    address = models.CharField(default='', max_length=100)


# 产品表
class Goods(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=2, default='')
    create_time = models.DateTimeField(default=timezone.now)
    goodsType_id = models.ForeignKey(GoodsType, related_name='goods_goods_type_id', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img', default='')
    single_price = models.DecimalField(decimal_places=2, max_digits=10)
    img = models.ImageField(upload_to='img/%Y/%m/%d', storage=ImageStorage())  # 如果上传文件可以将ImageField换为FileField


# 供应商表
class Cart(models.Model):
    goods_id = models.ForeignKey(Goods, related_name="cart_goods_id", on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)
    cr_us_id = models.ForeignKey(User, related_name="cart_user_id", on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    goods_name = models.CharField(default='', max_length=50)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)


class Desk(models.Model):
    name = models.CharField(max_length=10)
    status = models.CharField(max_length=10, default='')


# 信息表
class Msg(models.Model):
    # 信息名称
    name = models.CharField(max_length=10)
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now)
    # 信息级别
    level = models.CharField(max_length=10, default='')
    # 数量
    num = models.IntegerField(default=0)
    # 商品名称
    goods_name = models.CharField(max_length=100, default='')
    # 商品ID
    goods_id = models.ForeignKey(Goods, related_name='msg_goods_id', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


# 订单表
class Order(models.Model):
    order_code = models.CharField(max_length=50, default='', unique=True)
    status = models.CharField(max_length=5, default='')
    create_time = models.DateTimeField(default=timezone.now)
    bussnessDate = models.DateField(default=timezone.now)
    user_id = models.ForeignKey(User, related_name='order_user_id', on_delete=models.CASCADE)
    mark = models.CharField(max_length=100, default='')
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    total_profit = models.DecimalField(decimal_places=2, max_digits=10)
    delivery = models.CharField(max_length=100, default='')


# 订单详情表
class OrderDetail(models.Model):
    goods_id = models.ForeignKey(Goods, related_name='order_detail_goods_id', on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=20)
    num = models.IntegerField()
    sale_price = models.DecimalField(decimal_places=2, max_digits=10)
    goodsType_id = models.ForeignKey(GoodsType, related_name='order_detail_goods_type_id', on_delete=models.CASCADE)
    goodsType_Name = models.CharField(max_length=20, default='')
    order_id = models.ForeignKey(Order, max_length=50, related_name='order_detail_order_id', to_field='order_code',
                                 on_delete=models.CASCADE)
