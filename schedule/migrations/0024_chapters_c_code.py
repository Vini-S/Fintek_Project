# Generated by Django 2.2.2 on 2019-07-06 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0023_auto_20190706_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='c_code',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.Course'),
        ),
    ]
