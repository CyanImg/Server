# Generated by Django 3.0.3 on 2020-04-08 07:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0005_auto_20200408_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='reg_time',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 7, 2, 36, 32956, tzinfo=utc)),
        ),
    ]
