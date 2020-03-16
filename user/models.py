from django.db import models
from django.utils.timezone import now


class user(models.Model):
    def user_id(self):
        return self.id

    group_id = models.IntegerField(default=2)
    usercomment_id = models.IntegerField(null=True)
    address_id = models.IntegerField(null=True)
    user_name = models.CharField(default="小明", max_length=20)
    user_password = models.CharField(default="123456", max_length=256)
    email = models.EmailField(default="xxx@xxx.com")
    user_school = models.CharField(default="SWPU", max_length=20)
    pic = models.ImageField(null=True)
    small_pic = models.ImageField(null=True)
    reg_time = models.DateField(default=now())
    last_login_time = models.DateField(auto_now=True)
    userlikecomment_id = models.IntegerField(null=True)
    user_rename = models.CharField(null=True, max_length=20)
    user_repassword = models.CharField(null=True, max_length=20)


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
    album = models.ImageField()
    pic = models.ImageField(null=True)
    small_pic = models.ImageField(null=True)
    reg_time = models.DateField(default=now())
    last_login_time = models.DateField(auto_now=True)
    graphlikecomment_id = models.IntegerField(null=True)
    graph_rename = models.CharField(null=True,max_length=20)
    graph_repassword = models.CharField(null=True,max_length=256)


class comments(models.Model):
    def comment_id(self):
        return self.id

    group_id = models.IntegerField
    user_name = models.CharField(max_length=20)
    graph_name = models.CharField(max_length=20)
    user_school = models.CharField(max_length=20)
    graph_school = models.CharField(max_length=20)
    photo = models.ImageField


class like(models.Model):
    user_id = models.IntegerField
    likecomment_id = models.IntegerField