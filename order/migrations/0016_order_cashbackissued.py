# Generated by Django 3.0.8 on 2020-08-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20200816_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cashBackIssued',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
