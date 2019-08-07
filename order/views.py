from django.shortcuts import render, HttpResponse

import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  order.models import Order
from orderdetail.models import OrderDetail
from io import BytesIO
import time  # 引入time模块
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from sale.models import GoodsType
from goods.models import Goods
from cart.models import Cart

# 分页查询所有的供应商信息
@login_required
def queryOrderList(request):
    orders = Order.objects.all().order_by('-id')
    paginator = Paginator(orders, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    merchants_list = contacts.object_list
    return render(request, 'order/order_list.html', locals())


# 进入点餐界面
@login_required
def toOrderFood(request):
    # 查询所有的商品分类
    goodsTypes = GoodsType.objects.all()
    # 根据商品分类查询对应的商品
    goods_list_disc = []
    for item in goodsTypes:
        goods_list = Goods.objects.filter(goodsType_id_id=item.id)
        goods_list_disc.append(goods_list)
    return render(request, 'order/order_food.html', locals())


# 删除商品类型
@login_required
def delete(request, id):
    Order.objects.filter(id=id).delete()
    return HttpResponseRedirect('/queryOrderList/')


@login_required
def toAdd(request):
    return render(request, 'order/add.html');


# 添加
@login_required
@csrf_exempt
def add_order(request):
    order_code = get_order_code()
    customer_id_id = request.POST.get('customer_id_id', 'customer_id_id')
    description = request.POST.get('description', 'description')
    code = request.POST.get('code', 'code')
    user_id_id = request.POST.get('user_id_id', 'user_id_id')
    total_price = request.POST.get('total_price', 0)
    delivery = request.POST.get('delivery', 'delivery')
    mark = request.POST.get('mark', '无')
    bussnessDate = request.POST.get('bussnessDate', 'bussnessDate')
    nums = request.POST.getlist('num')
    goods_id = request.POST.getlist('goods_id')
    goods_names = request.POST.getlist('goods_name')
    print(request.POST)
    merchant_id_id = 1
    sale_price = 1
    Order.objects.create(order_code=order_code, bussnessDate=bussnessDate, customer_id_id=customer_id_id,
                         user_id_id=user_id_id, total_price=total_price, status='ZC', mark=mark, delivery=delivery)
    for i in range(0, len(nums)):
        OrderDetail.objects.create(goods_name=goods_names[i], num=nums[i], goods_id_id=goods_id[i],
                                   order_id_id=order_code, merchant_id_id=merchant_id_id, sale_price=sale_price)
    return JsonResponse({'status': 'ok'})


# 生成订单号
def get_order_code():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(time.time()).replace('.', '')[-7:]
    return order_no


# 查看今日销售笔数
@login_required
@csrf_exempt
def queryTodayOrder(request):
    date_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print('当前的时间为：',date_now)
    orders = Order.objects.filter(bussnessDate=date_now, status='ZC')
    today_add_order_count = len(orders)
    print('今日新增订单数量：',today_add_order_count)
    todayTotalAmount = Decimal(0.0)
    for item in orders:
        todayTotalAmount += item.total_price
    total_amount_of_month = Decimal(0.0)
    total_amount_of_year= Decimal(0.0)
    total_profit_of_month=Decimal(0.0)
    total_profit_of_year= Decimal(0.0)

    all_datas_month = Order.objects.filter(bussnessDate__month=date_now[5:7],status='ZC')
    all_datas_year = Order.objects.filter(bussnessDate__year=date_now[0:4],status='ZC')

    print("本月销售订单数量：",len(all_datas_month),'当前月份：',date_now[5:7])
    for item in all_datas_month:
        total_amount_of_month += item.total_price
        total_profit_of_month+=item.total_profit
    for item in all_datas_year:
        total_amount_of_year += item.total_price
        total_profit_of_year+=item.total_profit
    #本月销售毛利=本月销售总额-本月销售成本（商品进价*销售数量）

    print('本月销售毛利：', total_profit_of_month)
    print('本月销售总额：', total_amount_of_month)
    print('本年销售总额：', total_amount_of_year)
    return HttpResponse(json.dumps(
        {'today_add_order_count': today_add_order_count, 'todayTotalAmount': str(todayTotalAmount),  'total_amount_of_month': str(total_amount_of_month),
         'total_orders_month': len(all_datas_month),'total_amount_of_year': str(total_amount_of_year), 'total_profit_of_month':str(total_profit_of_month),'total_profit_of_year':str(total_profit_of_year)}))


@login_required
@csrf_exempt
def printOrder(request):
    date_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    user_id = request.user.id
    cart_list = Cart.objects.filter(cr_us_id_id=user_id)
    total_money = Decimal(0.0)
    for goods in cart_list:
        goods_db = Goods.objects.filter(id=goods.goods_id_id)
        total_money += goods.num * goods_db[0].single_price
    Cart.objects.all().delete()
    return render(request, 'order/print2.html', locals())
