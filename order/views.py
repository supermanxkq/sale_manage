from django.shortcuts import render, HttpResponse

import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  order.models import Order
from orderdetail.models import OrderDetail
from io import BytesIO
import time  # 引入time模块
from django.contrib.auth.decorators import login_required
from decimal import Decimal

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
    return render(request, 'order/list.html', locals())


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
    nums=request.POST.getlist('num')
    goods_id=request.POST.getlist('goods_id')
    goods_names=request.POST.getlist('goods_name')
    print(request.POST)
    merchant_id_id=1
    sale_price=1
    Order.objects.create(order_code=order_code, bussnessDate=bussnessDate, customer_id_id=customer_id_id,
                         user_id_id=user_id_id, total_price=total_price, status='ZC', mark=mark, delivery=delivery)
    for i in range(0,len(nums)):
        OrderDetail.objects.create(goods_name=goods_names[i], num=nums[i], goods_id_id=goods_id[i],
                                   order_id_id=order_code,merchant_id_id=merchant_id_id,sale_price=sale_price)
    return JsonResponse({'status': 'ok'})


# 生成订单号
def get_order_code():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(time.time()).replace('.', '')[-7:]
    return order_no



# 查看今日销售笔数
@login_required
@csrf_exempt
def queryTodayOrder(request):
    date_now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print(date_now)
    orders=Order.objects.filter(bussnessDate=date_now,status='ZC')
    count=len(orders)
    todayTotalAmount=Decimal(0.0)
    for item in orders:
        todayTotalAmount+=item.total_price
    orders_all = Order.objects.filter(status='ZC')
    total_amount=Decimal(0.0)
    for item in orders_all:
        total_amount+=item.total_price
    total_orders=len(orders_all)
    return HttpResponse(json.dumps({'count': count,'todayTotalAmount':str(todayTotalAmount),'total_amount':str(total_amount),'total_orders':total_orders}))
