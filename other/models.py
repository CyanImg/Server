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
class other(models.Model):
    def other_id(self):
        return self.id

    graphcomment_id = models.IntegerField(null=True)
    other_name = models.CharField(default="ssa",max_length=20)
    other_password = models.CharField(default="23456",max_length=256)
    other_school = models.CharField(default="pku",max_length=20)
    email = models.EmailField(default="xxx@xxx.com")
    other_identification = models.CharField(max_length=18)
    experience = models.CharField(max_length=1000)
    album = models.ImageField(null=True)
    pic = models.ImageField(null=True)
    small_pic = models.ImageField(null=True)
    reg_time = models.DateField(auto_now_add=True)
    last_login_time = models.DateField(auto_now=True)
    otherlikecomment_id = models.IntegerField(null=True)
    other_rename = models.CharField(null=True,max_length=20)
    other_repassword = models.CharField(null=True,max_length=256)
    forget_code = models.CharField(null=False, max_length=5, default=make_forget_code)
    verify_code = models.CharField(null=False, max_length=5, default=make_verify_code)
    is_verified = models.BooleanField(default=False)
