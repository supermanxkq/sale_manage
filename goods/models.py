from django.db import models
import django.utils.timezone as timezone
from sale.models import GoodsType
from system.storage import ImageStorage

#产品表
class Goods(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=2, default='')
    create_time = models.DateTimeField(default=timezone.now)
    goodsType_id= models.ForeignKey(GoodsType,related_name='goods_goods_type_id',on_delete=models.CASCADE)
    goodsType_Name= models.CharField(max_length=20, default='')
    img = models.ImageField(upload_to='img',default='')
    single_price = models.DecimalField(decimal_places=2, max_digits=10)
    wholesale_pice = models.DecimalField(decimal_places=2, max_digits=10)
    img = models.ImageField(upload_to='img/%Y/%m/%d', storage=ImageStorage())  # 如果上传文件可以将ImageField换为FileField



