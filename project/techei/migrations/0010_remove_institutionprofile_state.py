# Generated by Django 2.2.6 on 2019-10-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0009_auto_20191020_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institutionprofile',
            name='state',
        ),
    ]
