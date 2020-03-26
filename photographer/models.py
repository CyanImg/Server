from django.db import models
from django.utils.timezone import now

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
