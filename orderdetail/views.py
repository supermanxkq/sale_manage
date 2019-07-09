from django.shortcuts import render, HttpResponse

import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  orderdetail.models import OrderDetail
from io import BytesIO
import xlwt
# 分页查询所有的供应商信息
def queryOrderDetailList(request,order_code):
    print('order_code=',order_code)
    # order_code=request.POST.get("order_code")
    merchants = OrderDetail.objects.filter(order_id_id=order_code).order_by('id')
    paginator=Paginator(merchants,10)
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
    return render(request, 'orderdetail/order_detail.html', locals())

