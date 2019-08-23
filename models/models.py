from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser
from system.storage import ImageStorage


# 产品类型表
class GoodsType(models.Model):
    name = models.CharField(verbose_name='商品类型名称', max_length=10)
    description = models.CharField(default='', verbose_name='类型描述', max_length=500)
    code = models.CharField(max_length=10, unique=True, default='', verbose_name='代码')


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='权限标题', max_length=32)
    url = models.CharField(verbose_name='资源的URL', max_length=128)
    # 用来做控制，一些小权限（非菜单）么有就不显示
    name = models.CharField(verbose_name='URL别名', max_length=32, unique=True)  # unique唯一
    # menu = models.ForeignKey(verbose_name='所属一级菜单', help_text='null表示不是菜单，否则为二级菜单', null=True, blank=True, to='Menu',
    #                          on_delete=models.CASCADE)

    # 跟自身表关联，已经是菜单的就可以不关联null=True
    # 非菜单的权限，要选一个母菜单。当选中该权限时就可以归类跳转到母菜单下
    # pid = models.ForeignKey(verbose_name='关联的权限', to='Permission', null=True, blank=True, related_name='parents',
    #                         help_text='非菜单的权限，要选一个母菜单。当选中该权限时就可以归类跳转到母菜单下', on_delete=models.CASCADE)

class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)


class User(AbstractUser):
    img = models.ImageField(upload_to='img', default='', verbose_name='用户头像的URL')
    phone = models.CharField(max_length=11, unique=True, default='', verbose_name='手机号码')
    birthday = models.DateField(auto_now_add=True, verbose_name='生日')
    interests = models.CharField(default='', max_length=100, verbose_name='爱好')
    address = models.CharField(default='', max_length=100, verbose_name='所在地址')
    roles = models.ManyToManyField(verbose_name='拥有的所有的角色', to=Role, blank=True) # blank=True字段可以为空，=FALSE，字段必须填写


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
    bussnessDate = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, related_name='order_user_id', on_delete=models.CASCADE)
    mark = models.CharField(max_length=100, default='')
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    desk_id = models.ForeignKey(Desk, related_name='order_desk_id', on_delete=models.CASCADE)


# 订单详情表
class OrderDetail(models.Model):
    goods_id = models.ForeignKey(Goods, related_name='order_detail_goods_id', on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=20)
    num = models.IntegerField()
    sale_price = models.DecimalField(decimal_places=2, max_digits=10)
    order_id = models.ForeignKey(Order, max_length=50, related_name='order_detail_order_id', to_field='order_code',
                                 on_delete=models.CASCADE)


# 打印机设置
class Printer(models.Model):
    goodsType_id = models.ForeignKey(GoodsType, related_name='printer_goods_type_id', on_delete=models.CASCADE,
                                     verbose_name='商品分类编号')
    printer_name = models.CharField(max_length=50, default='', verbose_name='打印机名称')
    ip_address = models.CharField(max_length=20, default='', verbose_name='打印机IP地址')
    where_use = models.CharField(max_length=20, default='', verbose_name='使用地方')
    is_default = models.CharField(max_length=20, default='', verbose_name='是否默认打印机')
    device_type = models.CharField(max_length=20, default='', verbose_name='设备类型')
