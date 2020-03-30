from django.db import models
from django.utils.timezone import now

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
    reg_time = models.DateField(default=now())
    last_login_time = models.DateField(auto_now=True)
    otherlikecomment_id = models.IntegerField(null=True)
    other_rename = models.CharField(null=True,max_length=20)
    other_repassword = models.CharField(null=True,max_length=256)
