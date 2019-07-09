from django import template
from merchant.models import Merchant
from sale.models import GoodsType
from orderdetail.models import OrderDetail
from goods.models import Goods
from customer.models import Customer
register = template.Library()


@register.filter(is_safe=True)
def money_format(value):
    return format(value, '0,.2f')


@register.filter(is_safe=True)
def num_format(value):
    return format(value, ',')


@register.filter(is_safe=True)
def query_merchant_by_id(value):
    merchant=Merchant.objects.get(pk=value)
    return merchant.name

@register.filter(is_safe=True)
def query_goodsType_by_id(value):
    goodsType=GoodsType.objects.get(pk=value)
    return goodsType.name


# 根据订单编号，查询订单中商品的图片
@register.filter(is_safe=True)
def query_img_by_orderId(value):
    orderDetails=OrderDetail.objects.filter(order_id_id=value)
    imgHtml=''
    for item in orderDetails:
        # print(item.goods_id_id)
        goods=Goods.objects.get(pk=item.goods_id_id)
        imgHtml+='<img src='+str(goods.img)+' width=20px height=20px class="img-circle"/>'
    return imgHtml


@register.filter(is_safe=True)
def query_CustomerName_by_id(value):
    customer=Customer.objects.get(pk=value)
    return customer.name
