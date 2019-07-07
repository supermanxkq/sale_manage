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
import time;  # 引入time模块

# 分页查询所有的供应商信息
def queryOrderList(request):
    orders = Order.objects.all().order_by('id')
    paginator=Paginator(orders, 10)
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
def delete(request, id):
    Order.objects.filter(id=id).delete()
    return HttpResponseRedirect('/queryOrderList/')



def toAdd(request):
    return render(request, 'order/add.html');


# 添加
def add_order(request):
    order_code=get_order_code()
    customer_id_id = request.POST.get('customer_id_id', 'customer_id_id')
    description = request.POST.get('description', 'description')
    code = request.POST.get('code', 'code')
    user_id_id=request.POST.get('user_id_id','user_id_id')
    total_price=request.POST.get('total_price',0)
    delivery=request.POST.get('delivery','delivery')
    mark=request.POST.get('mark','无')
    bussnessDate=request.POST.get('bussnessDate','bussnessDate')
    print(bussnessDate,"param")
    Order.objects.create(order_code=order_code,bussnessDate=bussnessDate,customer_id_id=customer_id_id,user_id_id=user_id_id,total_price=total_price,status='ZC',mark=mark,delivery=delivery)
    # OrderDetail.objects.create()
    return HttpResponseRedirect('/queryOrderList/')

    # 生成订单号


def get_order_code():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(time.time()).replace('.', '')[-7:]
    return order_no
