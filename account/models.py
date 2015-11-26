#coding=utf-8
from django.db import models


class AccountStore(models.Model):
    account_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    actived = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_account_store'


class AccountName(models.Model):
    account_name = models.CharField(primary_key=True, max_length=32)
    account_id = models.PositiveIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_account_name'



class AccountProfile(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    avatar = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_account_profile'


class AccountFortune(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    money = models.PositiveIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_account_fortune'





