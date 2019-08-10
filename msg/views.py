from django.shortcuts import render, HttpResponse

import json
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from io import BytesIO
from django.core import serializers
import xlwt
from django.contrib.auth.decorators import login_required
from models.models import Msg

@login_required
@csrf_exempt
def queryMsgList(request):
    json_data = serializers.serialize("json", Msg.objects.all().order_by('-create_time'))
    return HttpResponse(json_data, content_type='application/json')


@login_required
def queryMsgListPage(request):
    merchants = Msg.objects.all().order_by('id')
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
    return render(request, 'msg/msg_list.html', locals())