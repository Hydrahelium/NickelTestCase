# Generated by Django 2.2.3 on 2019-07-03 23:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timefeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name_plural': 'Stock timeline',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=64, verbose_name='Компания')),
                ('stock_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена акции')),
                ('timestamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_time', to='awesome_nornik_stocks.Timefeed')),
            ],
            options={
                'verbose_name_plural': 'Stocks',
            },
        ),
    ]
