from django.shortcuts import render, HttpResponse
import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models.models import Goods
from models.models import GoodsType
from sale_manage import settings
import os
from django.core import serializers
from io import BytesIO
import xlwt
from django.contrib.auth.decorators import login_required
from system.storage import ImageStorage


# 分页查询所有的供应商信息
@login_required
def list_page(request):
    goods = Goods.objects.all().order_by('-id')
    paginator = Paginator(goods, 7)
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
    return render(request, 'goods/goods_list.html', locals())


@login_required
def delete(request, id):
    Goods.objects.filter(id=id).delete()
    return HttpResponseRedirect('/goods_list_page/')


@login_required
def goods_update(request):
    goods_id = request.POST.get('goodsId', 'goodsId')
    name = request.POST.get('name', 'name')
    img = request.POST.get('img', 'img')
    status = request.POST.get('status', 'status')
    single_price = request.POST.get('single_price', 'single_price')
    goodsType_id_id = request.POST.get('goodsType_id_id', 'goodsType_id_id')
    file_obj = request.FILES.get('file')
    goods_old = Goods.objects.get(pk=goods_id)
    if file_obj:
        if '/static/img/upload_files/' + file_obj.name != goods_old.img:
            print('获取到的图片和数据库中保存的不一样：file_obj.name:', file_obj.name)
            imgStorage = ImageStorage()
            name_save = imgStorage.save(file_obj.name, file_obj)
            img = '/static/img/upload_files/' + name_save

    Goods.objects.filter(id=goods_id).update(name=name, img=img,  status=status,
                                             single_price=single_price, goodsType_id_id=goodsType_id_id)
    return HttpResponseRedirect('/goods_list_page/')


@login_required
def toAdd(request):
    return render(request, 'goods/goods_add.html');


@csrf_exempt
@login_required
def add(request):
    file_obj = request.FILES.get('file')
    if file_obj:
        imgStorage = ImageStorage()
        name_save = imgStorage.save(file_obj.name, file_obj)
        img = '/static/img/upload_files/' + name_save
        name = request.POST.get('name', 'name')
        status = request.POST.get('status', 'status')
        single_price = request.POST.get('single_price', 'single_price')
        goodsType_id_id = request.POST.get('goodsType_id_id', 'goodsType_id_id')
        Goods.objects.create(name=name, img=img, status=status,
                             single_price=single_price, goodsType_id_id=goodsType_id_id )
    return HttpResponseRedirect('/goods_list_page/')


# 查询所有商品信息
@csrf_exempt
@login_required
def queryGoodsNameList(request):
    json_data = serializers.serialize("json", Goods.objects.all().order_by('id'))
    return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
@login_required
def queryGoodsById(request):
    goodsId = request.POST.get('goodsId')
    json_data = serializers.serialize("json", Goods.objects.filter(pk=goodsId))
    return HttpResponse(json_data, content_type='application/json')


@login_required
def goods_edit(request, id):
    goods = Goods.objects.get(pk=id)
    status_list = [{'value': 'ZC', 'text': '正常'}, {'value': 'XJ', 'text': '下架'}]
    goodstype_list = GoodsType.objects.all()
    return render(request, 'goods/goods_edit.html', locals());
