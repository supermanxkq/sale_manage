from django.shortcuts import render, HttpResponse
from sale.models import User
from sale.models import GoodsType
import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from sale_manage import settings
import  os
# login frame
def login_page(request):
    return render(request, 'login.html');


# 首页
@login_required
def index(request):
    return render(request, 'index.html');


# 登录
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 确保用户名和密码都不为空
    if username and password:
        username = username.strip()
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            auth.login(request, user)
            is_authenticated = request.user.is_authenticated
            print(is_authenticated)
            if is_authenticated:
                return HttpResponse(json.dumps({'status': 1001, 'msg': '认证成功！'}))
        else:
            return HttpResponse(json.dumps({'status': 1003, 'error': '用户名或密码错误！'}))


# 跳转到注册页面
def to_sign_up(request):
    return render(request, 'signUp.html');


# 注册用户
@csrf_exempt
def sign_up(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    result = User.objects.filter(username=username)
    print(result)
    if result:
        return JsonResponse({'message': 'username is already exists !!!'})
    else:
        file_obj = request.FILES.get('file')
        print(file_obj,'ooooooooo')
        if file_obj:
            accessory_dir = settings.MEDIA_ROOT
            if not os.path.isdir(accessory_dir):
                os.mkdir(accessory_dir)
            upload_file = "%s/%s" % (accessory_dir, file_obj.name)
            with open(upload_file, 'wb') as new_file:
                for chunk in file_obj.chunks():
                    new_file.write(chunk)
        img = '/static/img/upload_files/' + file_obj.name

        User.objects.create_user(username=username, password=password,img=img)
        return JsonResponse({'username': username, 'message': 'regist ok!'})


def check_login(request):
    is_authenticated = request.user.is_authenticated
    if is_authenticated:
        return HttpResponse(json.dumps({'status': 1001, 'msg': '认证成功！'}))
    else:
        return HttpResponse(json.dumps({'status': 1002, 'msg': '认证失败！'}))


# 用户退出
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/loginPage')



# 获取个人信息
@login_required
def get_user_info(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'userinfo.html', object_to_json(user));
    # return JsonResponse(object_to_json(user))


# objects.get()结果转换
def object_to_json(obj):
    return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])


# 更新用户的信息
@login_required
def update_user_info(request):
    user_id = request.POST.get('id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    print('获取到的参数是：user_id,first_name,last_name', user_id, first_name, last_name, email)
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
    User.objects.filter(id=user_id).update(first_name=first_name, last_name=last_name, email=email,img=img)
    return HttpResponseRedirect('/')


# 商品类型列表
@login_required
def goodsTypeList(request):
    name = request.GET.get('name')
    goods_Types = GoodsType.objects.all().order_by('-id');
    if name:
        goods_Types = GoodsType.objects.filter(name=name)
    paginator = Paginator(goods_Types, 10)  # Show 7 contacts per page
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    goods_Types_List = contacts.object_list
    return render(request, 'goods_type/goodsType.html', locals())


# 删除商品类型
@login_required
def del_goods_type(request, id):
    GoodsType.objects.filter(id=id).delete()
    return HttpResponseRedirect('/goodsTypeList/')


@login_required
def goodstype_edit(request, id):
    goods_type = GoodsType.objects.get(id=id)
    return render(request, 'goods_type/goodstype_edit.html', {
        'Data': goods_type,
    });


@login_required
def goodstype_update(request):
    print('进入了更新的方法！')
    id = request.POST.get('id', 'id')
    name = request.POST.get('name', 'nameID')
    description = request.POST.get('description', 'description')
    code = request.POST.get('code', 'code')
    goods_type = GoodsType.objects.filter(id=id).update(name=name, description=description, code=code)
    return HttpResponseRedirect('/goodsTypeList/')


@login_required
def to_add_goods_type(request):
    return render(request, 'goods_type/goodstype_add.html');


@login_required
def goods_type_add(request):
    name = request.POST.get('name', 'nameID')
    description = request.POST.get('description', 'description')
    code = request.POST.get('code', 'code')
    GoodsType.objects.create(name=name, description=description, code=code)
    return HttpResponseRedirect('/goodsTypeList/')


@login_required
@csrf_exempt
def query_goodstype_list(request):
    json_data = serializers.serialize('json', GoodsType.objects.all())
    return HttpResponse(json_data, content_type='application/json')

@login_required()
def toUpPwd(request):
    return render(request,'update_pwd.html')

# @login_required
# def updatePwd(request):
#     id = request.POST.get('id', 'id')
#     pwd = request.POST.get('password', 'password')
#     User.objects.filter(id=id).update(password=pwd)
#     return HttpResponseRedirect('/index/')



# 修改密码
@login_required
def updatePwd(request):
    username = request.POST.get('username', None)
    oldPassword = request.POST.get('oldPassword',None)
    newPassword = request.POST.get('newPassword',None)
    print(oldPassword,newPassword,username,'xxxxxxxx')
    changeResult = db_change_password(username, oldPassword, newPassword)
    return HttpResponse(changeResult)


# 修改密码
@login_required
def db_change_password(username, oldPassword, newPassword):
    user = authenticate(username=username, password=oldPassword)
    if user is not None:
        if user.is_active:
            user.set_password(newPassword)
            user.save()
            return 1    # 修改成功，允许特殊符号
        else:
            return -2   # 没有权限
    else:
        return -1      # 旧密码错误
