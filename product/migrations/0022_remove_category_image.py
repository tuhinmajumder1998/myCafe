# Generated by Django 3.0.8 on 2020-09-01 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20200826_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
