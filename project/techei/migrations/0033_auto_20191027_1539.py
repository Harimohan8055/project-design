# Generated by Django 2.2.6 on 2019-10-27 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0032_auto_20191027_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
