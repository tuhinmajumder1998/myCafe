# Generated by Django 3.0.8 on 2020-07-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
    ]
