# Generated by Django 2.2.6 on 2019-10-20 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0006_auto_20191019_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='state',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
