# Generated by Django 3.0.8 on 2020-08-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
