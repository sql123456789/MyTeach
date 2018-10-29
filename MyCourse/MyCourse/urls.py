# encoding=utf-8
"""MyCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
# 处理Django的media文件
from django.views.static import serve
import xadmin
from users.views import LoginView,RegisterView,ActivUserView,ForGetPwdView,ResetUserView,ModifyPwdView
from organization.views import OrgView
from MyCourse.settings import MEDIA_ROOT
from organization import urls

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',TemplateView.as_view(template_name="index.html"),name="index"),
    url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'^register/$',RegisterView.as_view(),name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActivUserView.as_view(),name='user_active'),
    url(r'^forget/$',ForGetPwdView.as_view(),name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$',ResetUserView.as_view(),name='reset_pwd'),
    url(r'^modify_pwd/$',ModifyPwdView.as_view(),name="modify_pwd"),
    # 课程url的配置
    url(r'^org/',include('organization.urls',namespace='org')),

    # 配置media文件的取出路径,配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)/$',serve,{"document_root":MEDIA_ROOT}),
]
