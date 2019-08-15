from django.shortcuts import render, HttpResponse

import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import sys, base64
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  models.models import Order
from models.models import OrderDetail
from io import BytesIO
import time  # 引入time模块
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from models.models import GoodsType
from models.models import Goods
from models.models import Cart
from models.models import Desk
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtPrintSupport import QPrinter, QPrinterInfo
from PyQt5.QtGui import QPainter, QImage
import sys, base64
from system.Printer import Printer
import sys
from PyQt5.QtWidgets import QApplication
from django.utils import timezone
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
def OrderFood(request,desk_id):
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
def add_order(request, desk_id):
    # 该桌号下是否有未结账订单
    order_pre = Order.objects.filter(desk_id_id=desk_id, status='YTJ')
    if order_pre:
        order = order_pre[0]
        # 根据用户ID获取用户的购物车商品
        cart_list = Cart.objects.filter(cr_us_id=request.user.id)
        total_price = Decimal(0.0)
        for cart in cart_list:
            total_price += cart.sale_price * cart.num
        # 更新订单的总金额
        order.total_price += total_price
        order.save()
        # 添加订单详情
        for cart in cart_list:
            OrderDetail.objects.create(goods_name=cart.goods_name, num=cart.num, goods_id_id=cart.goods_id_id,
                                       order_id_id=order.order_code, sale_price=cart.sale_price)
    else:
        # 新增新的订单
        # 获取界面传递的参数
        order_code = get_order_code()
        user_id_id = request.user.id
        time_now = timezone.now().strftime("%Y-%m-%d %H:%I:%S");
        # 根据用户ID获取用户的购物车商品
        cart_list=Cart.objects.filter(cr_us_id=user_id_id)
        # 逻辑出添加订单的必要参数
        total_price=Decimal(0.0)
        for cart in cart_list:
            total_price += cart.sale_price*cart.num
        # 添加订单信息
        Order.objects.create(order_code=order_code, desk_id_id=desk_id, bussnessDate=time_now, user_id_id=user_id_id, total_price=total_price, status='YTJ', mark="无")
        # 添加订单详情的信息
        for cart in cart_list:
            OrderDetail.objects.create(goods_name=cart.goods_name, num=cart.num, goods_id_id=cart.goods_id_id,
                                       order_id_id=order_code,  sale_price=cart.sale_price)
    # 清空购物车中的商品信息
    Cart.objects.all().delete()

    # 更新桌台的状态为用餐中
    desk = Desk.objects.get(id=desk_id)
    desk.status = 'YCZ'
    desk.save()
    return render(request, 'order/print_order.html', locals())


# 生成订单号
def get_order_code():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
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
    app = QApplication(sys.argv)
    data_url=request.POST.get('data_url')
    new_data_url=data_url.replace('data:image/png;base64,', '')
    # print(new_data_url)
    p = "DL-581PW"  # 打印机名称
    # Printer.printing(p, html)
    # Printer.printerList()
    # printer=Printer()
    # printerInfo = QPrinterInfo()
    # printer.print_(new_data_url, p)
    # printing_22(request,p,  new_data_url)
    # sys.exit(app.exec_())
    return HttpResponse(json.dumps({'result':'ok'}))


# @login_required
# def printing_22(request,printer, context):
#     printerInfo = QPrinterInfo()
#     p = QPrinter()
#     for item in printerInfo.availablePrinters():
#         if printer == item.printerName():
#             p = QPrinter(item)
#             doc = QTextDocument()
#             doc.setHtml(u'%s' % context)
#             doc.setPageSize(QSizeF(p.logicalDpiX()*(297/25.4),
#             p.logicalDpiY()*(297/25.4)))
#             p.setOutputFormat(QPrinter.NativeFormat)
#             doc.print_(p)
