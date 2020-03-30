# Generated by Django 3.0.3 on 2020-03-28 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphcomment_id', models.IntegerField(null=True)),
                ('other_name', models.CharField(default='ssa', max_length=20)),
                ('other_password', models.CharField(default='23456', max_length=256)),
                ('other_school', models.CharField(default='pku', max_length=20)),
                ('email', models.EmailField(default='xxx@xxx.com', max_length=254)),
                ('other_identification', models.CharField(max_length=18)),
                ('experience', models.CharField(max_length=1000)),
                ('album', models.ImageField(null=True, upload_to='')),
                ('pic', models.ImageField(null=True, upload_to='')),
                ('small_pic', models.ImageField(null=True, upload_to='')),
                ('reg_time', models.DateField(default=datetime.datetime(2020, 3, 28, 9, 13, 33, 262165, tzinfo=utc))),
                ('last_login_time', models.DateField(auto_now=True)),
                ('otherlikecomment_id', models.IntegerField(null=True)),
                ('other_rename', models.CharField(max_length=20, null=True)),
                ('other_repassword', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
