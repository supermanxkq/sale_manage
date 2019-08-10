from django import template
from models.models import GoodsType
from models.models import OrderDetail
from models.models import Goods

register = template.Library()
import datetime


@register.filter(is_safe=True)
def money_format(value):
    return format(value, '0,.2f')


@register.filter(is_safe=True)
def num_format(value):
    return format(value, ',')





@register.filter(is_safe=True)
def query_goodsType_by_id(value):
    goodsType = GoodsType.objects.get(pk=value)
    return goodsType.name


# 根据订单编号，查询订单中商品的图片
@register.filter(is_safe=True)
def query_img_by_orderId(value):
    orderDetails = OrderDetail.objects.filter(order_id_id=value)
    imgHtml = ''
    for item in orderDetails:
        # print(item.goods_id_id)
        goods = Goods.objects.get(pk=item.goods_id_id)
        imgHtml += '<img src=' + str(goods.img) + ' width=20px height=20px class="img-circle"/>'
    return imgHtml




@register.filter(is_safe=True)
def time_passed(value):
    now = datetime.now()
    past = now - value
    if past.days:
        return u'%s天前' % past.days
    mins = past.seconds / 60
    if mins < 60:
        return u'%s分钟前' % mins
    hours = mins / 60
    return u'%s小时前' % hours


@register.filter(is_safe=True)
def query_single_price_by_id(value):
    goods = Goods.objects.get(pk=value)
    return goods.single_price


@register.filter(is_safe=True)
def calc_total(num, goods_id):
    goods = Goods.objects.get(pk=goods_id)
    return goods.single_price * num


