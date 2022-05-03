# Generated by Django 3.1 on 2022-04-14 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payhistory',
            name='paystack_access_code',
        ),
        migrations.RemoveField(
            model_name='payhistory',
            name='paystack_charge_id',
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='verification_expires',
            field=models.DateField(default=datetime.date(2022, 4, 17)),
        ),
    ]
