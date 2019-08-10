from django.shortcuts import render, HttpResponse
import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  models.models import Desk
from io import BytesIO
import xlwt
from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required
def desk_list_page(request):
    desks = Desk.objects.all().order_by('id')
    paginator=Paginator(desks, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    desks_list = contacts.object_list
    return render(request, 'desk/desk_list.html', locals())



@login_required
def delete_desk(request, id):
    desk=Desk.objects.get(id=id)
    desk.status='YSC'
    desk.save()
    return HttpResponseRedirect('/desk_list_page/')

@login_required
def desk_edit(request, id):
    desk = Desk.objects.get(id=id)
    return render(request, 'desk/desk_update.html', locals());

@login_required
def desk_update(request):
    id=request.POST.get('id')
    name = request.POST.get('name', 'name')
    status=request.POST.get('status','status')
    Desk.objects.filter(id=id).update(name=name, status=status)
    return HttpResponseRedirect('/desk_list_page/')


@login_required
def to_desk_add(request):
    return render(request, 'desk/desk_add.html');

# 注册用户
@csrf_exempt
@login_required
def add_desk(request):
    name = request.POST.get('name', 'name')
    Desk.objects.create(name=name, status="YCJ")
    return HttpResponseRedirect('/desk_list_page/')
@login_required
def export(request):
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=customers.xls'
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
    sheet.write(0, 1, '客户名称', style_heading)
    sheet.write(0, 2, '手机号码', style_heading)
    sheet.write(0, 3, '来自', style_heading)
    sheet.write(0, 4, '备注', style_heading)

    # 写入数据
    data_row = 1
    # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
    for i in Customer.objects.all():
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
def  query_customer_list(request):
    json_data=serializers.serialize('json', Customer.objects.all())
    return HttpResponse(json_data, content_type='application/json')
