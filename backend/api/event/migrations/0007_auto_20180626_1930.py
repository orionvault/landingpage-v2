# Generated by Django 2.0.6 on 2018-06-26 19:30

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20180626_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='cert',
            field=models.FileField(upload_to=event.models.get_file_path, verbose_name='Certificate file'),
        ),
    ]
