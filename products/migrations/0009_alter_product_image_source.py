# Generated by Django 3.2 on 2022-03-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_image_url_product_image_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
