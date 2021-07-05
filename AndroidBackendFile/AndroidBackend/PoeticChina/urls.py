"""AndroidBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 分布式路由系统中的子 路由文件
# from django.contrib import admin
from django.urls import path, include
from . import views

# 指明当前可服务的地址
# path函数的第二个参数为 视图函数
# 视图函数接受浏览器的请求（HttpRequest对象），处理后向浏览器返回HttpResponse对象
# 视图函数定义在 项目同名目录下，同urls在同一个目录

# 可以使用path转换器
urlpatterns = [
    path('index', views.index_view),
    path('poems', views.poems_view),
    path('poets', views.poets_view),
    path('poet_representworks', views.poet_works_view),
    path('upload_poems', views.upload_poem_view),
    path('upload_poets', views.upload_poet_view),
    path('collect_poem', views.collect_poem_view),
    path('un_collect_poem', views.un_collect_poem_view),
    path('search_collect_status', views.search_collect_status_view),
    path('collections', views.collections_view)
]
