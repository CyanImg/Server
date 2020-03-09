from django.db import models
from django.utils.timezone import now

class user(models.Model):
    def user_id(self):
        return self.id
    group_id = models.IntegerField(default=2)
    usercomment_id = models.IntegerField(null=True)
    address_id = models.IntegerField(null=True)
    user_name = models.CharField(default="小明",max_length=20)
    user_password = models.CharField(default="123456",max_length=256)
    email = models.EmailField(default="xxx@xxx.com")
    user_school = models.CharField(default="SWPU",max_length=20)
    pic = models.ImageField(null=True)
    small_pic = models.ImageField(null=True)
    reg_time = models.DateField(default=now())
    last_login_time = models.DateField(auto_now=True)
    userlikecomment_id = models.IntegerField(null=True)
    user_rename = models.CharField(null=True,max_length=20)
    user_repassword = models.CharField(null=True,max_length=20)
# Create your models here.
