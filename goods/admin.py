from django.contrib import admin
from goods.models import Goods
from goods.models import GoodsType
# Register your models here.
admin.site.register(Goods)
admin.site.register(GoodsType)