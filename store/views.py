from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  store.models import Store
from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# 分页查询所有的供应商信息
@login_required
def list_page(request):
    goods_name = request.GET.get('goods_name', '')
    merchants = Store.objects.all().order_by('-create_time')
    if goods_name:
        # Q(goods_name__icontains=goods_name)
        merchants = Store.objects.filter(goods_name=goods_name)
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
    return render(request, 'store/list.html', locals())

@login_required
# 删除商品类型
def delete(request, id):
    Store.objects.filter(id=id).delete()
    return HttpResponseRedirect('/store_list_page/')

@login_required
def toEdit(request, id):
    goods_type = Store.objects.get(id=id)
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
    goods_type = Store.objects.filter(id=id).update(name=name, description=description, code=code)
    return HttpResponseRedirect('/goodsTypeList/')

@login_required
def toAdd(request):
    return render(request, 'store/add.html');

@login_required
@csrf_exempt
def add(request):
    goods_name = request.POST.get('goods_name', 'goods_name')
    num = request.POST.get('num', 'num')
    total_price = request.POST.get('total_price', 'total_price')
    single_price = request.POST.get('single_price', 'single_price')
    goods_id_id = request.POST.get('goods_id_id', 'goods_id_id')
    Store.objects.create(goods_name=goods_name, num=num, total_price=total_price, single_price=single_price, goods_id_id=goods_id_id)
    return HttpResponseRedirect('/store_list_page/')


