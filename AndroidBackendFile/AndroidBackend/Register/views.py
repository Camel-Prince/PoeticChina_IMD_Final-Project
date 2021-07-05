from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from Login.models import Login
import json
from django.db import transaction
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        already_registered = {
            'username': username,
            'password': password,
            # 'adminname': '',
            'code': '错误，用户已经存在',
            'Status Code': 404
        }
        try:
            user = Login.objects.create(username=username, password=password)
            data = {
                'username': user.username,
                'password': password,
                # 'adminname': user.adminname,
                'code': '成功',
                'Status Code': 200
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        except IntegrityError:
            # 重名注册请求会被回滚；
            transaction.rollback()
            return HttpResponse(json.dumps(already_registered), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')

