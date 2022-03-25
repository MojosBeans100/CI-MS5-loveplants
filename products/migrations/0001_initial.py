# Generated by Django 3.2 on 2022-03-25 20:06

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(max_length=100)),
                ('latin_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('description_source', models.CharField(blank=True, max_length=100, null=True)),
                ('description_url', models.URLField(blank=True, null=True)),
                ('image_url', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('pot_size', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('maturity_num', models.PositiveIntegerField(blank=True, null=True)),
                ('maturity_time', models.CharField(blank=True, choices=[('weeks', 'weeks'), ('months', 'months'), ('years', 'years')], max_length=15, null=True)),
                ('sunlight', models.CharField(blank=True, choices=[('low', 'low'), ('med', 'med'), ('high', 'high')], max_length=15, null=True)),
                ('watering', models.CharField(blank=True, choices=[('low', 'low'), ('med', 'med'), ('high', 'high')], max_length=15, null=True)),
                ('care_required', models.BooleanField(blank=True, choices=[('low', 'low maintenance'), ('high', 'high maintenance')], null=True)),
                ('rare', models.BooleanField(blank=True, null=True)),
                ('popular', models.BooleanField(blank=True, null=True)),
                ('out_of_stock', models.BooleanField(blank=True, null=True)),
                ('returning_soon', models.BooleanField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
            options={
                'ordering': ['-stock_quantity'],
            },
        ),
    ]