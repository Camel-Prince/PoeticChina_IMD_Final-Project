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
# 主路由文件
from django.contrib import admin
from django.urls import path, re_path, include
from . import views as main_views
from Login import views as login_views
from Register import views as register_views
# 指明当前可服务的地址
# path函数的第二个参数为 视图函数
# 视图函数接受浏览器的请求（HttpRequest对象），处理后向浏览器返回HttpResponse对象
# 视图函数定义在 项目同名目录下，同urls在同一个目录

# 可以使用path转换器
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/001', main_views.page1_view),
    path('page/<int:pg_index>', main_views.pagen_view),
    path('test_template/', main_views.test_template),
    path('PoeticChina/', include('PoeticChina.urls')),
    path('login', login_views.login_view),
    path('register', register_views.register_view),
]
