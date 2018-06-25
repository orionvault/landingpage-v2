# Generated by Django 2.0.6 on 2018-06-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallpaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_code', models.CharField(max_length=6, verbose_name='PIN Code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
            ],
            options={
                'verbose_name': 'Wallpaper',
                'verbose_name_plural': 'Wallpapers',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='WallpaperImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image file')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('device', models.CharField(choices=[('hd', 'HD'), ('uhd', 'UHD'), ('iphone6', 'iPhone 6'), ('iphone6plus', 'iPhone 6+'), ('iphone7', 'iPhone 7'), ('iphone7plus', 'iPhone 7+'), ('iphone8', 'iPhone 8'), ('iphone8plus', 'iPhone 8+'), ('iphonex', 'iPhone X'), ('samsung_s8', 'Samsung S8/S8 Plus'), ('samsung_s9', 'Samsung S9/S9 Plus')], max_length=12, verbose_name='Target device')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
            ],
            options={
                'verbose_name': 'Wallpaper Image',
                'verbose_name_plural': 'Wallpaper Images',
                'ordering': ['created_at'],
            },
        ),
    ]
