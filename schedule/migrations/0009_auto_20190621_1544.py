# Generated by Django 2.2.2 on 2019-06-21 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_chapters_f_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_view',
            old_name='c_code_id',
            new_name='c_code',
        ),
        migrations.RemoveField(
            model_name='admin_view',
            name='A_leave',
        ),
        migrations.RemoveField(
            model_name='faculty_view',
            name='l_id',
        ),
        migrations.RemoveField(
            model_name='faculty_view',
            name='m_id',
        ),
        migrations.RemoveField(
            model_name='faculty_view',
            name='s_id',
        ),
        migrations.RemoveField(
            model_name='faculty_view',
            name='se_id',
        ),
        migrations.RemoveField(
            model_name='student_view',
            name='s_course',
        ),
        migrations.AddField(
            model_name='admin_view',
            name='A_leave_accept',
            field=models.CharField(default='', max_length=100, verbose_name='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin_view',
            name='A_leave_reject',
            field=models.CharField(default='', max_length=100, verbose_name='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty_view',
            name='Password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='leave',
            name='f_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.Faculty_view'),
        ),
        migrations.AddField(
            model_name='leave',
            name='s_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.Student_view'),
        ),
        migrations.AddField(
            model_name='session',
            name='f_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.Faculty_view'),
        ),
        migrations.AddField(
            model_name='student_view',
            name='Password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
