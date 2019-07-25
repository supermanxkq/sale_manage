from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  purchase.models import Purchase
from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from store.models import Store


@login_required
def purchase_list_page(request):
    goods_name = request.GET.get('goods_name', '')
    merchants = Purchase.objects.all().order_by('-create_time')
    if goods_name:
        # Q(goods_name__icontains=goods_name)
        merchants = Purchase.objects.filter(goods_name=goods_name)
    paginator = Paginator(merchants, 10)
    page = request.GET.get('page')

    print('keywords:',goods_name)

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    merchants_list = contacts.object_list
    return render(request, 'purchase/purchase_list.html', locals())

@login_required
# 删除商品类型
def delete_purchase(request, id):
    Purchase.objects.filter(id=id).delete()
    return HttpResponseRedirect('/purchase_list_page/')\

@login_required
def addToStore(request, purchase_id):
    print('采购单的ID为：',purchase_id)
    purchase_obj=Purchase.objects.get(pk=purchase_id)
    print('获取到的采购单实体为:',purchase_obj.goods_name)
    # 查询库存中该商品，如果有，将数量累加，如果没有，新建数据
    goods_in_store=Store.objects.filter(goods_id_id=purchase_obj.goods_id_id)
    print('获取到的库存中的商品信息为：',goods_in_store)
    if goods_in_store:
        print('进入了更新数量的方法',goods_in_store[0].num)
        goods_in_store[0].num+=purchase_obj.num
        goods_in_store[0].total_price+=purchase_obj.total_price
        goods_in_store[0].save()
    else:
        Store.objects.create(goods_name=purchase_obj.goods_name, num=purchase_obj.num, total_price=purchase_obj.total_price, single_price=purchase_obj.single_price,
                             goods_id_id=purchase_obj.goods_id_id)
    # 更改采购单的状态为已入库
    purchase_obj.status='YRK'
    purchase_obj.save()
    return HttpResponseRedirect('/purchase_list_page/')

@login_required
def toEdit(request, id):
    goods_type = Purchase.objects.get(id=id)
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
    goods_type = Purchase.objects.filter(id=id).update(name=name, description=description, code=code)
    return HttpResponseRedirect('/goodsTypeList/')

@login_required
def toPurchaseAdd(request):
    return render(request, 'purchase/purchase_add.html');

@login_required
@csrf_exempt
def add_purchase(request):
    goods_name = request.POST.get('goods_name', 'goods_name')
    num = request.POST.get('num', 'num')
    total_price = request.POST.get('total_price', 'total_price')
    single_price = request.POST.get('single_price', 'single_price')
    goods_id_id = request.POST.get('goods_id_id', 'goods_id_id')
    Purchase.objects.create(goods_name=goods_name, num=num,status='WRK', total_price=total_price, single_price=single_price, goods_id_id=goods_id_id)
    return HttpResponseRedirect('/purchase_list_page/')


