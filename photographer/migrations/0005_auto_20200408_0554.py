# Generated by Django 3.0.3 on 2020-04-08 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0004_auto_20200403_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='reg_time',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 5, 54, 10, 379466, tzinfo=utc)),
        ),
    ]
