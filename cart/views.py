from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from goods.models import Goods
import json
from django.core import serializers
from decimal import Decimal
from order.models import Order
from orderdetail.models import OrderDetail
import time


@login_required
@csrf_exempt
def addShopCart(request):
    goods_id = request.POST.get('goods_id')
    num = request.POST.get('num')
    cr_us_id = request.user.id
    goods_name = request.POST.get('goods_name')
    sale_price=request.POST.get('sale_price')
    print(sale_price)
    Cart.objects.create(num=num, cr_us_id_id=cr_us_id, goods_id_id=goods_id, goods_name=goods_name,sale_price=sale_price)
    return HttpResponse(json.dumps({'stauts': 1}))


@login_required
@csrf_exempt
def query_cart_list(request):
    user_id = request.user.id
    cart_list = Cart.objects.filter(cr_us_id_id=user_id)
    json_data = serializers.serialize('json', cart_list)
    return HttpResponse(json_data, content_type='application/json')


@login_required
def toConfirmOrder(request):
    user_id = request.user.id
    cart_list = Cart.objects.filter(cr_us_id_id=user_id)
    total_money = Decimal(0.0)
    for goods in cart_list:
        goods_db = Goods.objects.filter(id=goods.goods_id_id)
        total_money += goods.num * goods_db[0].single_price
    return render(request, 'cart/confirm_cart.html', locals())


@login_required
def submitOrder(request):
    user_id_id = request.user.id
    order_code = get_order_code()

    cart_list=Cart.objects.filter(id=user_id_id)
    for goods_in_cart in cart_list:
        OrderDetail.objects.create(goods_name=goods_in_cart.goods_name, num=goods_in_cart.num, goods_id_id=goods_in_cart.goods_id_id,
                                   order_id_id=order_code, merchant_id_id=1, sale_price=0)
    customer_id_id = request.POST.get('customer_id_id', 'customer_id_id')
    total_price = request.POST.get('total_price', 0)
    delivery = request.POST.get('delivery', 'delivery')
    mark = request.POST.get('mark', '无')
    bussnessDate = request.POST.get('bussnessDate', 'bussnessDate')
    nums = request.POST.getlist('num')
    goods_id = request.POST.getlist('goods_id')
    goods_names = request.POST.getlist('goods_name')
    merchant_id_id = 1
    sale_price = 1
    Order.objects.create(order_code=order_code, bussnessDate=bussnessDate, customer_id_id=customer_id_id,
                         user_id_id=user_id_id, total_price=total_price, status='ZC', mark=mark, delivery=delivery)
    for i in range(0, len(nums)):
        OrderDetail.objects.create(goods_name=goods_names[i], num=nums[i], goods_id_id=goods_id[i],
                                   order_id_id=order_code, merchant_id_id=merchant_id_id, sale_price=sale_price)
    Order.objects.create()


# 生成订单号
def get_order_code():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(time.time()).replace('.', '')[-7:]
    return order_no



@login_required
@csrf_exempt
def delete_cart(request,id):
    # pk=request.POST.get('id')
    # print(pk,'pk sssss')
    Cart.objects.filter(pk=id).delete()
    return HttpResponse(json.dumps({'status': 1}))
