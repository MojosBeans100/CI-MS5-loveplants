# Generated by Django 3.2 on 2022-03-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_image_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_source',
            new_name='image1_source',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_source_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image1_source_url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image2_source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image2_source_url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image3_source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image3_source_url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
