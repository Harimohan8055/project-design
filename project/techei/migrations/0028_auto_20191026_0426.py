# Generated by Django 2.2.6 on 2019-10-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0027_auto_20191025_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='end_date',
            field=models.DateField(auto_now_add=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='start_date',
            field=models.DateField(auto_now_add=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='time',
            field=models.TimeField(auto_now_add=True, max_length=15),
        ),
    ]