# Generated by Django 3.0.8 on 2020-08-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20200808_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription_duration',
            name='price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
