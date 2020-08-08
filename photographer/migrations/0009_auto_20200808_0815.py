# Generated by Django 2.2.7 on 2020-08-08 08:15

from django.db import migrations, models
import photographer.models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0008_auto_20200605_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='forget_code',
            field=models.CharField(default=photographer.models.make_forget_code, max_length=5),
        ),
        migrations.AddField(
            model_name='photographer',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='photographer',
            name='verify_code',
            field=models.CharField(default=photographer.models.make_verify_code, max_length=5),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='reg_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
