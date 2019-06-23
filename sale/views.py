from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
import json
from django.contrib import auth
from django.http import JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core import serializers
# 登录皆灭
def login_page(request):
    return render(request, 'login.html');


# 首页
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
        User.objects.create_user(username=username, password=password)
        return JsonResponse({'username': username, 'message': 'regist ok!'})

# 用户退出
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/loginPage')

#个人信息
def to_person_info(request):
    return render(request, 'userinfo.html');

#获取个人信息
def  get_user_info(request):
    user=User.objects.get(username=request.user.username)
    print('获取到的当前登录的用户为：',type(user))
    return JsonResponse(object_to_json(user))

# objects.get()结果转换
def object_to_json(obj):
    return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])


