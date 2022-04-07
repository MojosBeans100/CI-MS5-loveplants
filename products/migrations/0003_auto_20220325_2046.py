# Generated by Django 3.2 on 2022-03-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220325_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Height (cm)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Length (cm)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pot_size',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Pot size (cm)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price (£)'),
        ),
    ]