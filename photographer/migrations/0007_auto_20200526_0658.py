# Generated by Django 3.0.3 on 2020-05-26 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0006_auto_20200408_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='reg_time',
            field=models.DateField(default=datetime.datetime(2020, 5, 26, 6, 58, 6, 53807, tzinfo=utc)),
        ),
    ]