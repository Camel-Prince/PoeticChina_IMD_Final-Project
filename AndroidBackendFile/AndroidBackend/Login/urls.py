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
    # path('Login', views.login_view)
]