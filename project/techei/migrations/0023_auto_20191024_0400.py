# Generated by Django 2.2.6 on 2019-10-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0022_auto_20191024_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festclubmodel',
            name='description',
            field=models.TextField(),
        ),
    ]