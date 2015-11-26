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

        #1 获取注册用户名、邮箱和密码
        account_name = d.get('account_name', None)
        email = d.get('email', None)
        password = d.get('password', None)
        logger = logging.getLogger('op')
        logger.info(u'Register::post %s' %unicode(d))
 
        #2 判断邮箱是否已经注册
        try: 
            o_account_name = AccountName.objects.get(account_name=account_name)
        except ObjectDoesNotExist:
            o_account_name = None

        try: 
            o_account_store = AccountStore.objects.get(email=email)
        except ObjectDoesNotExist:
            o_account_store = None

        if o_account_name:
            kwargs['error'] = True
            kwargs['info'] = u'账号:%s已被占用' %account_name
            t = TemplateResponse(request, 'account/register.html', kwargs)
            return t
 
        if o_account_store:
            kwargs['error'] = True
            kwargs['info'] = u'邮箱:%s已经注册' %email
            t = TemplateResponse(request, 'account/register.html', kwargs)
            return t
 
        o_account_store = AccountStore()
        o_account_store.email = email
        o_account_store.password = password
        o_account_store.save()
        o_account_name = AccountName()
        o_account_name.account_name = account_name
        o_account_name.account_id = o_account_store.account_id
        o_account_name.save()

        # 放入Rabbitmq工作队列中
        send_mail(u'激活邮件', u'测试激活邮件', u'拍工作<noreply@paigongzuo.com>', [email,], fail_silently=False)
        msg = u'send active email'
        print msg
        t = TemplateResponse(request, 'account/register_finish.html', kwargs)
        return t
 
       

