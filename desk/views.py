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
    paginator = Paginator(desks, 10)
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
    desk = Desk.objects.get(id=id)
    desk.status = 'YSC'
    desk.save()
    return HttpResponseRedirect('/desk_list_page/')


@login_required
def desk_edit(request, id):
    desk = Desk.objects.get(id=id)
    return render(request, 'desk/desk_update.html', locals());


@login_required
def desk_update(request):
    id = request.POST.get('id')
    name = request.POST.get('name', 'name')
    status = request.POST.get('status', 'status')
    Desk.objects.filter(id=id).update(name=name, status=status)
    return HttpResponseRedirect('/desk_list_page/')


@login_required
def to_desk_add(request):
    return render(request, 'desk/desk_add.html');


@csrf_exempt
@login_required
def add_desk(request):
    name = request.POST.get('name', 'name')
    Desk.objects.create(name=name, status="YCJ")
    return HttpResponseRedirect('/desk_list_page/')


@login_required
def to_desk_status_list(request):
    desks=Desk.objects.all()
    return render(request, 'desk/desk_status_list.html', locals())

@login_required
@csrf_exempt
def open_desk(request):
    desk_id=request.POST.get("desk_id","id")
    desk=Desk.objects.get(id=desk_id)
    desk.status='YKT'
    desk.save()
    return HttpResponse(json.dumps({'status':'ok'}))


