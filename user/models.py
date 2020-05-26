from django.db import models


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
    pic = models.ImageField(null=True, upload_to='icon')
    small_pic = models.ImageField(null=True, upload_to='icon_small')
    reg_time = models.DateField(auto_now_add=True)
    last_login_time = models.DateField(auto_now=True)
    userlikecomment_id = models.IntegerField(null=True)
    user_rename = models.CharField(null=True, max_length=20)
    user_repassword = models.CharField(null=True, max_length=20)


class comments(models.Model):
    def comment_id(self):
        return self.id

    group_id = models.IntegerField
    user_name = models.CharField(max_length=20)
    graph_name = models.CharField(max_length=20)
    user_school = models.CharField(max_length=20)
    graph_school = models.CharField(max_length=20, null=True)
    comment_content = models.CharField(max_length=144)
    photo = models.ImageField(null=True)


class like(models.Model):
    user_id = models.IntegerField
    likecomment_id = models.IntegerField


class order(models.Model):
    def order_id(self):
        return self.id

    user_name = models.CharField(max_length=20)
    graph_name = models.CharField(max_length=20)
    order_time = models.DateField(auto_now_add=True)
    total = models.IntegerField(max_length=10)
    update_time = models.DateField(auto_now=True)
    order_status = models.BooleanField(default=False)  # False == not finished
    payment_status = models.BooleanField(default=False)  # False == not paid
    meet_time = models.DateField(auto_now_add=False,auto_now=False,null=False)
    address = models.CharField(max_length=256)
    tel = models.CharField(max_length=11)
    user_school = models.CharField(max_length=20)
    graph_school = models.CharField(max_length=20)