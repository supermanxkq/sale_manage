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
from msg.models import Msg

@login_required
@csrf_exempt
def queryMsgList(request):
    json_data = serializers.serialize("json", Msg.objects.all().order_by('-create_time'))
    return HttpResponse(json_data, content_type='application/json')
