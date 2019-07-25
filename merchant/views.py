from django.shortcuts import render, HttpResponse
import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  merchant.models import Merchant
from io import BytesIO
from django.core import serializers
import xlwt
from django.contrib.auth.decorators import login_required


@login_required
# 分页查询所有的供应商信息
def list_page(request):
    merchants = Merchant.objects.all().order_by('id')
    paginator = Paginator(merchants, 10)
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
    return render(request, 'merchant/merchant_list.html', locals())


@login_required
# 删除商品类型
def delete(request, id):
    Merchant.objects.filter(id=id).delete()
    return HttpResponseRedirect('/merchant_list_page/')


@login_required
def merchant_edit(request, id):
    merchant = Merchant.objects.get(id=id)
    return render(request, 'merchant/merchant_update.html',locals());


@login_required
def merchant_update(request):
    id = request.POST.get('id')
    name = request.POST.get('name', 'name')
    phone = request.POST.get('phone', 'phone')
    mark = request.POST.get('mark', 'mark')
    address = request.POST.get('address', 'address')
    where_from = request.POST.get('where_from', 'where_from')
    Merchant.objects.filter(id=id).update(name=name, phone=phone, mark=mark, address=address, where_from=where_from)
    return HttpResponseRedirect('/merchant_list_page/')


@login_required
def toAdd(request):
    return render(request, 'merchant/merchants_add.html');


@login_required
@csrf_exempt
def add(request):
    name = request.POST.get('name', 'name')
    phone = request.POST.get('phone', 'phone')
    mark = request.POST.get('mark', 'mark')
    address = request.POST.get('address', 'address')
    where_from = request.POST.get('where_from', 'where_from')
    Merchant.objects.create(name=name, phone=phone, mark=mark, address=address, where_from=where_from)
    return HttpResponseRedirect('/merchant_list_page/')


@login_required
def export(request):
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=merchant.xls'
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('order-sheet')

    # 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
    style_heading = xlwt.easyxf("""
               font:
                   name Arial,
                   colour_index white,
                   bold on,
                   height 0xA0;
               align:
                   wrap off,
                   vert center,
                   horiz center;
               pattern:
                   pattern solid,
                   fore-colour 0x19;
               borders:
                   left THIN,
                   right THIN,
                   top THIN,
                   bottom THIN;
               """)

    # 写入文件标题
    sheet.write(0, 0, '序号', style_heading)
    sheet.write(0, 1, '供应商名称', style_heading)
    sheet.write(0, 2, '手机号码', style_heading)
    sheet.write(0, 3, '来自', style_heading)
    sheet.write(0, 4, '备注', style_heading)

    # 写入数据
    data_row = 1
    # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
    for i in Merchant.objects.all():
        # 格式化datetime
        sheet.write(data_row, 0, i.id)
        sheet.write(data_row, 1, i.name)
        sheet.write(data_row, 2, i.phone)
        sheet.write(data_row, 3, i.where_from)
        sheet.write(data_row, 4, i.mark)
        data_row += 1
    # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response


@login_required
@csrf_exempt
def queryMerchants(request):
    json_data = serializers.serialize("json", Merchant.objects.all().order_by('id'))
    return HttpResponse(json_data, content_type='application/json')
