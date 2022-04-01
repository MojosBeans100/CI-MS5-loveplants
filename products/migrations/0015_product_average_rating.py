# Generated by Django 3.2 on 2022-04-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_productreview_review_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
