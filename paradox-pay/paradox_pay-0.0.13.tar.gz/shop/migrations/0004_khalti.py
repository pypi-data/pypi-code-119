# Generated by Django 3.1 on 2022-05-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_esewa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Khalti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(blank=True, max_length=150, null=True)),
                ('private_key', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
