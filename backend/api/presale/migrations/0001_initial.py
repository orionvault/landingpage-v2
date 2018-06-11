# Generated by Django 2.0.6 on 2018-06-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PresaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last name')),
                ('residency', models.CharField(max_length=100, verbose_name='Residency')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('currency', models.CharField(choices=[('usd', 'USD'), ('btc', 'BTC'), ('eth', 'ETH')], default='usd', max_length=3, verbose_name='Currency')),
                ('contribution', models.FloatField(verbose_name='Contribution')),
                ('investor_type', models.CharField(choices=[('individual', 'Individual person'), ('investor', 'Accreditated investor'), ('fund', 'Fund')], default='individual', max_length=11, verbose_name='Investor type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
            ],
            options={
                'verbose_name_plural': 'Presale Orders',
                'ordering': ['last_name'],
                'verbose_name': 'Presale Order',
            },
        ),
    ]
