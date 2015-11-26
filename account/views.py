#coding=utf-8
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import * 
import logging
# Create your views here.

class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        d = request.GET
        t = TemplateResponse(request, 'account/login.html', kwargs)
        return t

class Register(TemplateView):
    def get(self, request, *args, **kwargs):
        d = request.GET
        t = TemplateResponse(request, 'account/register.html', kwargs)
        return t

    def post(self, request, *args, **kwargs):
        d = request.POST

        #1 获取注册用户名和密码
        email = d.get('email', None)
        password = d.get('password', None)
        logger = logging.getLogger('op')
        print d
        logger.error(d)
 
        #2 判断邮箱是否已经注册
        try:
            a = AccountStore.objects.get(email=email)
            kwargs['error'] = True
            kwargs['info'] = u'邮箱已经注册'
            t = TemplateResponse(request, 'account/register.html', kwargs)
            return t
        except ObjectDoesNotExist:

            # 放入Rabbitmq工作队列中
            send_mail(u'激活邮件', u'测试激活邮件', u'拍工作<noreply@paigongzuo.com>', [email,], fail_silently=False)
            msg = u'send active email'
            print msg
            t = TemplateResponse(request, 'account/register_finish.html', kwargs)
            return t
 
       

