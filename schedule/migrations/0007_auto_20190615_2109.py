# Generated by Django 2.2.2 on 2019-06-15 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_remove_users_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_view',
            old_name='c_code',
            new_name='c_code_id',
        ),
        migrations.RemoveField(
            model_name='chapters',
            name='c_code',
        ),
        migrations.RemoveField(
            model_name='course',
            name='s_id',
        ),
        migrations.RemoveField(
            model_name='student_view',
            name='f_id',
        ),
        migrations.RemoveField(
            model_name='student_view',
            name='l_id',
        ),
    ]
