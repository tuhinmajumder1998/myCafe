# Generated by Django 3.0.8 on 2020-08-08 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0006_subscription_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription_duration',
            old_name='Subscription',
            new_name='subscription',
        ),
    ]