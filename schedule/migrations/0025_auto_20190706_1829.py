# Generated by Django 2.2.2 on 2019-07-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0024_chapters_c_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_leave',
            name='f_status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='student_leave',
            name='s_status',
            field=models.CharField(default='', max_length=10),
        ),
    ]
