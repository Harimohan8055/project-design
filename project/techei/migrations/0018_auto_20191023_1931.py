# Generated by Django 2.2.6 on 2019-10-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0017_auto_20191023_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festimage',
            name='name',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
