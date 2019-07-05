from django import template
from merchant.models import Merchant
from sale.models import GoodsType
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