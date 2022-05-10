# Generated by Django 3.2 on 2022-05-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_product_plant_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='length',
        ),
        migrations.AlterField(
            model_name='product',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='care_required',
            field=models.CharField(choices=[('can stand a little neglect', 'low maintenance'), ('requires frequent care', 'high maintenance')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.PositiveIntegerField(default=0, verbose_name='Height (cm)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image1_source_url',
            field=models.URLField(default='www.example@example.com', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image2_source',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='latin_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='maturity_num',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='maturity_time',
            field=models.CharField(choices=[('weeks', 'weeks'), ('months', 'months'), ('years', 'years')], default='weeks', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='plant_category',
            field=models.CharField(choices=[('Potted', 'potted'), ('Hanging', 'hanging'), ('Floor', 'floor'), ('Flowers', 'flowers'), ('Succulents', 'succulents')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='pot_size',
            field=models.PositiveIntegerField(default=0, verbose_name='Pot size (cm)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='sunlight',
            field=models.CharField(choices=[('low', 'low'), ('med', 'med'), ('high', 'high')], default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='watering',
            field=models.CharField(choices=[('low', 'low'), ('med', 'med'), ('high', 'high')], default=0, max_length=15),
            preserve_default=False,
        ),
    ]