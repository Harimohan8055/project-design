# Generated by Django 2.2.6 on 2019-10-19 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0002_auto_20191019_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
    ]
