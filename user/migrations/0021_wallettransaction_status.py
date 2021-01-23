# Generated by Django 3.0.8 on 2020-08-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_wallettransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallettransaction',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Received', 'Received'), ('Failed', 'Failed')], default='Failed', max_length=10),
        ),
    ]