# Generated by Django 3.0.8 on 2020-08-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_subscriber_user_ends'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='TXNAMOUNT',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
