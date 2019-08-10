from django.shortcuts import render, HttpResponse
import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from io import BytesIO
import xlwt
from django.contrib.auth.decorators import login_required
from django.core import serializers
from models.models import OrderDetail
from django.db.models import Sum




@login_required
@csrf_exempt
def queryStatisticsData(request):
    result=OrderDetail.objects.values('goodsType_id','goodsType_Name').annotate(number=Sum("num"))
    nameList = []
    dataList = []
    objList=[]
    for item in result:
        nameList.append(item['goodsType_Name'])
        dataList.append(item['number'])
        objList.append({'value':item['number'],'name':item['goodsType_Name']})
    return HttpResponse(json.dumps({'nameList': nameList,'dataList':dataList,'objList':objList}))
