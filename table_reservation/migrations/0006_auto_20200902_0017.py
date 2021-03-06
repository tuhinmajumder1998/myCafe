# Generated by Django 3.0.8 on 2020-09-01 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table_reservation', '0005_auto_20200901_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='table_reserve',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table_reservation.Table'),
        ),
        migrations.AlterField(
            model_name='table_reserve',
            name='time_table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table_reservation.Time_Table'),
        ),
        migrations.AlterField(
            model_name='time_table',
            name='parent_table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='table_reservation.Table'),
        ),
    ]
