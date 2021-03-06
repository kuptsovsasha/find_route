# Generated by Django 3.1.3 on 2021-07-31 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0003_auto_20210728_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='train name')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='time on a road')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='from which city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='to which city')),
            ],
            options={
                'verbose_name': 'Train',
                'verbose_name_plural': 'Trains',
                'ordering': ['travel_time'],
            },
        ),
    ]
