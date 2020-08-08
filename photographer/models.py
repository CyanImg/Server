from django.db import models
from random import randint


def make_forget_code():
    dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ0123456789'
    code = ''
    for i in range(5):
        code += dic[randint(0, len(dic) - 1)]
    return code


def make_verify_code():
    dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ0123456789'
    code = ''
    for i in range(5):
        code += dic[randint(0, len(dic) - 1)]
    return code

class photographer(models.Model):
    def graph_id(self):
        return self.id

    graphcomment_id = models.IntegerField(null=True)
    group_id = models.IntegerField(default=1)
    graph_name = models.CharField(default="ssa",max_length=20)
    graph_password = models.CharField(default="23456",max_length=256)
    graph_school = models.CharField(default="pku",max_length=20)
    email = models.EmailField(default="xxx@xxx.com")
    graph_identification = models.CharField(max_length=18)
    experience = models.CharField(max_length=1000)
    album = models.ImageField(null=True)
    pic = models.ImageField(null=True)
    small_pic = models.ImageField(null=True)
    reg_time = models.DateField(auto_now_add=True)
    last_login_time = models.DateField(auto_now=True)
    graphlikecomment_id = models.IntegerField(null=True)
    graph_rename = models.CharField(null=True,max_length=20)
    graph_repassword = models.CharField(null=True,max_length=256)
    graph_device = models.CharField(null=True,max_length=20)
    forget_code = models.CharField(null=False, max_length=5, default=make_forget_code)
    verify_code = models.CharField(null=False, max_length=5, default=make_verify_code)
    is_verified = models.BooleanField(default=False)
