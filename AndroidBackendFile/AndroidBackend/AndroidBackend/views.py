from django.http import *
from django.shortcuts import render
# 注意，视图函数的第一个参数必须是 request，一点都不能变


def page1_view(request):
    print("Method: "+request.method)
    print("GET queryDict: ", request.GET)
    html = "<h1>This is first page</h1>" \
           "request.get: %s" % str(request.GET)
    return HttpResponse(html)


def pagen_view(request, pg_index):
    html = "<h1>This is %s page. 小轩我爱你哦～</h1>" % pg_index
    return HttpResponse(html)


# html文件的加载方式： 使用render：
def test_template(request):
    # 使用字典向html传递数据
    dic = {"name": "wzx", "npy_name": "mlx"}
    return render(request, 'test_template.html', dic)
