# Generated by Django 2.2.6 on 2019-10-26 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import techei.models


class Migration(migrations.Migration):

    dependencies = [
        ('techei', '0030_auto_20191026_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(blank=True, max_length=255, null=True, upload_to=techei.models.get_file_path_event)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techei.EventModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]