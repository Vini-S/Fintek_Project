# Generated by Django 2.2.2 on 2019-06-21 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20190615_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='f_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.Faculty_view'),
        ),
    ]
