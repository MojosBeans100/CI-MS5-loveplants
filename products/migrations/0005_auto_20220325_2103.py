# Generated by Django 3.2 on 2022-03-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='out_of_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='returning_soon',
        ),
        migrations.AddField(
            model_name='product',
            name='care_instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_source_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('in stock', 'In stock'), ('out of stock', 'Out of stock'), ('returning soon', 'Returning soon')], default='out of stock', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='care_required',
            field=models.CharField(blank=True, choices=[('low', 'low maintenance'), ('high', 'high maintenance')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_source',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
