from django.shortcuts import render, HttpResponse

import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  models.models import Order
from models.models import GoodsType
from io import BytesIO
import time  # 引入time模块
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from models.models import Printer
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinterInfo, QPrinter

@login_required
def printer_list_page(request):
    printers = Printer.objects.all().order_by('-id')
    paginator = Paginator(printers, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    printers_list = contacts.object_list
    return render(request, 'printer/printer_list.html', locals())


@login_required
def to_add_printer(request):
    goodsType_list=GoodsType.objects.all()
    printer_list=printerList(request)
    return render(request,'printer/printer_add.html', locals())


@login_required
def printer_add(request):
    printer_name=request.POST.get('printer_name')
    ip_address=request.POST.get('ip_address')
    where_use=request.POST.get('where_use')
    is_default=request.POST.get('is_default')
    device_type=request.POST.get('device_type')
    goodsType_id_id=request.POST.get('goodsType_id_id')
    Printer.objects.create(printer_name=printer_name,ip_address=ip_address,where_use=where_use,is_default=is_default,device_type=device_type,goodsType_id_id=goodsType_id_id)
    return HttpResponseRedirect('/printer_list_page/')

@login_required
def printerList(request):
    printer = []
    printerInfo = QPrinterInfo()
    print('availablePrinterNames', printerInfo.availablePrinterNames())
    print('defaultPrinterName', printerInfo.defaultPrinterName())

    for item in printerInfo.availablePrinters():
        printer.append(item.printerName())
    return printer

@login_required
def del_printer(request, id):
    Printer.objects.filter(id=id).delete()
    return HttpResponseRedirect('/printer_list_page/')