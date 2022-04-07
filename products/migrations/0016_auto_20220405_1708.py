# Generated by Django 3.2 on 2022-04-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_average_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='care_required',
            field=models.CharField(blank=True, choices=[('can stand a little neglect', 'low maintenance'), ('requires frequent care', 'high maintenance')], max_length=50, null=True),
        ),
    ]