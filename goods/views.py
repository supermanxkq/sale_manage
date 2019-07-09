from django.shortcuts import render, HttpResponse
import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  goods.models import Goods
from sale_manage import settings
import os
from django.core import serializers
from io import BytesIO
import xlwt
from django.contrib.auth.decorators import login_required


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
    return render(request, 'goods/list.html', locals())


# 删除商品类型
@login_required
def delete(request, id):
    Goods.objects.filter(id=id).delete()
    return HttpResponseRedirect('/goods_list_page/')

@login_required
def toEdit(request, id):
    goods_type = Goods.objects.get(id=id)
    return render(request, 'goodstype_edit.html', {
        'Data': goods_type,
    });

@login_required
def update(request):
    print('进入了更新的方法！')
    id = request.POST.get('id', 'id')
    name = request.POST.get('name', 'nameID')
    description = request.POST.get('description', 'description')
    code = request.POST.get('code', 'code')
    goods_type = Goods.objects.filter(id=id).update(name=name, description=description, code=code)
    return HttpResponseRedirect('/goodsTypeList/')

@login_required
def toAdd(request):
    return render(request, 'goods/add.html');


@csrf_exempt
@login_required
def add(request):
    file_obj = request.FILES.get('file')
    if file_obj:
        accessory_dir = settings.MEDIA_ROOT
        if not os.path.isdir(accessory_dir):
            os.mkdir(accessory_dir)
        upload_file = "%s/%s" % (accessory_dir, file_obj.name)
        with open(upload_file, 'wb') as new_file:
            for chunk in file_obj.chunks():
                new_file.write(chunk)
    img = '/static/img/upload_files/' + file_obj.name
    name = request.POST.get('name', 'name')
    status = request.POST.get('status', 'status')
    single_price = request.POST.get('single_price', 'single_price')
    goodsType_id_id = request.POST.get('goodsType_id_id', 'goodsType_id_id')
    merchant_id_id = request.POST.get('merchant_id_id', 'merchant_id_id')
    Goods.objects.create(name=name, img=img, status=status, single_price=single_price, goodsType_id_id=goodsType_id_id,
                         merchant_id_id=merchant_id_id)
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
    goodsId=request.POST.get('goodsId')
    json_data = serializers.serialize("json", Goods.objects.filter(pk=goodsId))
    return HttpResponse(json_data, content_type='application/json')