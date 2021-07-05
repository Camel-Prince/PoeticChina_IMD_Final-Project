import json

from django.db import IntegrityError, transaction
from django.http import HttpResponse
from django.shortcuts import render
from PoeticChina.models import Collect

# Create your views here.
# App相关的视图部分
from PoeticChina.models import Poem
from PoeticChina.models import Poet
from Login.models import Login


def index_view(request):
    dic = {"app_name": "诗意中国", "developer": "王子旭"}
    return render(request, 'PoeticChina/Index.html', dic)


def poems_view(request):
    if request.method == 'GET':
        poems = []
        for poem in Poem.objects.all():
            poems.append({
                'poem_title': poem.name,
                'poet_name': poem.poet.name,
                'poem_content': poem.content,
                'poem_img': poem.poem_img,
                'poem_time': poem.time,
                'poem_analysis': poem.analysis
            })
        data = {
            'poems': poems,
            'code': '成功获取所有诗歌',
            'Status Code': 200
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse('Post请求无效')


def poets_view(request):
    if request.method == 'GET':
        poets = []
        for poet in Poet.objects.all():
            poets.append({
                'name': poet.name,
                'introduction': poet.introduction,
                'img': poet.poet_img
            })
        data = {
            'poets': poets,
            'code': '成功获取所有诗人',
            'Status Code': 200
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse('Post请求无效')


def upload_poem_view(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        poet_name = request.POST.get('poet_name')
        content = request.POST.get('content')

        poet = Poet.objects.get(name=poet_name)
        poet_id = poet.id

        for aPoem in Poem.objects.all():
            if aPoem.content == content:
                data = {
                    'name': name,
                    'code': '失败',
                    'Status Code': 400
                }
                return HttpResponse(json.dumps(data), content_type='application/json')

        try:
            Poem.objects.create(name=name, poet_id=poet_id, content=content)
            data = {
                'name': name,
                'code': '成功',
                'Status Code': 200
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        except IntegrityError:

            transaction.rollback()
            return HttpResponse(json.dumps({
                'code': '失败',
                'Status Code': 404
            }), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')


def upload_poet_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        introduction = request.POST.get('introduction')
        try:
            Poet.objects.create(name=name, introduction=introduction)
            data = {
                'name': name,
                'code': '成功',
                'Status Code': 200
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        except IntegrityError:
            transaction.rollback()
            return HttpResponse(json.dumps({
                'code': '失败',
                'Status Code': 404
            }), content_type='application/json')
    else:
        return HttpResponse('GET请求无效')


def poet_works_view(request):
    if request.method == "POST":
        post_poet_name = request.POST.get("poet_name")
        poems = Poem.objects.all()
        error = {
            "works": [],
            "Status Code": 404
        }
        if len(poems) == 0:
            return HttpResponse(json.dumps(error), content_type='application/json')
        data = {
            "works": [],
            "Status Code": 200
        }
        for poem in poems:
            poet = poem.poet
            if poet.name == post_poet_name and len(data['works']) <= 3:
                data['works'].append(poem.name)

        return HttpResponse(json.dumps(data), content_type='application/json')


def collect_poem_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        poemname = request.POST.get("poemname")

        poem_obj = Poem.objects.get(name=poemname)
        user_obj = Login.objects.get(username=username)

        try:
            Collect.objects.create(user=user_obj, poem=poem_obj)
            data = {
                "Status Code": 200
            }

        except IntegrityError:
            transaction.rollback()
            data = {
                "Status Code": 400
            }
        return HttpResponse(json.dumps(data), content_type='application/json')


def un_collect_poem_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        poemname = request.POST.get("poemname")

        poem_obj = Poem.objects.get(name=poemname)
        user_obj = Login.objects.get(username=username)
        try:
            Collect.objects.get(user=user_obj, poem=poem_obj).delete()
            data = {
                "Status Code": 200
            }
        except IntegrityError:
            data = {
                "Status Code": 400
            }

        return HttpResponse(json.dumps(data), content_type='application/json')


def search_collect_status_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        poemname = request.POST.get("poemname")

        poem_obj = Poem.objects.get(name=poemname)
        user_obj = Login.objects.get(username=username)
        collect = Collect.objects.filter(user=user_obj, poem=poem_obj)
        if collect.count() != 1:
            data={
                "Status Code": 400
            }
        else:
            data={
                "Status Code": 200
            }
    return HttpResponse(json.dumps(data), content_type='application/json')


def collections_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user_obj = Login.objects.get(username=username)
        collect_rs = Collect.objects.filter(user=user_obj)
        poems = []
        if collect_rs.count() > 0:
            for row in collect_rs:
                poem = row.poem
                poems.append({
                    'poem_title': poem.name,
                    'poet_name': poem.poet.name,
                    'poem_content': poem.content,
                    'poem_img': poem.poem_img,
                    'poem_time': poem.time,
                    'poem_analysis':poem.analysis
                })
                data = {
                    'poems': poems,
                    'code': '成功获取所有收藏的诗歌',
                    'Status Code': 200
                }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                'poems': [],
                'Status Code': 404
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
