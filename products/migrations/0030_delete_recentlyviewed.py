# Generated by Django 3.2 on 2022-05-15 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_productreview_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecentlyViewed',
        ),
    ]
