from django.shortcuts import render

# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from .models import Login
import json


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        date_error = {
            'username': username,
            # 'adminname': '',
            'code': '错误，用户不存在',
            'Status Code': 404

        }
        try:
            user = Login.objects.get(username=username)
            if user.password == password:
                data = {
                    'username': user.username,
                    # 'adminname': user.adminname,
                    'code': '成功',
                    'Status Code': 200
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                date_error = {
                    'username': username,
                    # 'adminname': '',
                    'code': '密码错误',
                    'Status Code': 404
                }
                return HttpResponse(json.dumps(date_error), content_type='application/json')
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(date_error), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')
