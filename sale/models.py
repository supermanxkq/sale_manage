from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User

# 系统用户表
# class User(models.Model):
#     username = models.CharField(max_length=10)
#     password = models.CharField(max_length=20)
#     sign_up_time = models.DateTimeField('保存日期', default=timezone.now)
#     real_name = models.CharField('真实名字', max_length=10, default='')
#     phone = models.CharField(max_length=11, unique=True, verbose_name='手机号', default='')
#     job = models.CharField(max_length=20, default='')
#     email = models.EmailField(default='')
#     status = models.CharField(default='1', max_length=2)
#     create_id = models.IntegerField(default=0)
#     create_name=models.CharField(max_length=10,default='')
#     def __unicode__(self):
#         return self.name


# 系统角色表
# class Role(models.Model):
#     # 角色名称
#     name = models.CharField(max_length=10)
#     user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
#     user_name= models.CharField(max_length=10,default='')
#     description = models.CharField(max_length=20, default='')
#     create_time = models.DateTimeField(default=timezone.now)
#     status = models.CharField(max_length=2, default='')
#     role_code = models.CharField(max_length=10, default='')
#
#     def __unicode__(self):
#         return self.name


# 权限表

# 客户表
class Customer(models.Model):
    name = models.CharField(max_length=10)
    create_time = models.DateTimeField(default=timezone.now)
    where_from = models.CharField(max_length=10, default='')
    mark = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号', default='')
    address = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name

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


# 款项信息
# class PayInfo(models.Model):
#     pay_type=models.CharField(max_length=10)
#     customer_id = models.IntegerField(default=0)
#     create_time = models.DateTimeField(default=timezone.now)
#     description = models.CharField(default='',max_length=500)
#     money = models.DecimalField(decimal_places=2 , max_digits=10)
#     pay_method = models.CharField(max_length=10)
#     summary = models.CharField(max_length=500)

# 产品类型表
class GoodsType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(default='',max_length=500)
    code =models.CharField(max_length=10, default='')

#产品表
class Goods(models.Model):
    name = models.CharField(max_length=10)
    status = models.CharField(max_length=2, default='')
    create_time = models.DateTimeField(default=timezone.now)
    goodsType_id= models.ForeignKey(GoodsType,related_name='goods_goods_type_id',on_delete=models.CASCADE)
    goodsType_Name= models.CharField(max_length=20, default='')
    merchant_id= models.ForeignKey(Merchant,related_name='goods_mer_id', on_delete=models.CASCADE)
    single_price = models.DecimalField(decimal_places=2, max_digits=10)

#仓库表
class Store(models.Model):
    goods_id = models.ForeignKey(Goods,related_name='store_goods_id',on_delete=models.CASCADE)
    goods_name= models.CharField(max_length=10)
    num = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2 , max_digits=10)
    single_price = models.DecimalField(decimal_places=2, max_digits=10)

#订单表
class Order(models.Model):
    status = models.CharField(max_length=5, default='')
    create_time = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, related_name='order_user_id', on_delete=models.CASCADE)
    mark = models.CharField(max_length=100, default='')
    total_price = models.DecimalField(decimal_places=2, max_digits=10)

#订单详情表
class OrderDetail(models.Model):
    merchant_id = models.ForeignKey(Merchant, related_name='order_detail_mer_id', on_delete=models.CASCADE)
    goods_id = models.ForeignKey(Goods, related_name='order_detail_goods_id', on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=10)
    num = models.IntegerField()
    sale_price = models.DecimalField(decimal_places=2, max_digits=10)
    goodsType_id= models.ForeignKey(GoodsType,related_name='order_detail_goods_type_id',on_delete=models.CASCADE)
    goodsType_Name= models.CharField(max_length=20, default='')