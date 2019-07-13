# Generated by Django 2.2.2 on 2019-07-05 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_auto_20190704_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted_Faculty_leave',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_email', models.CharField(max_length=100)),
                ('a_s_date', models.DateField(max_length=100)),
                ('a_e_date', models.DateField(max_length=100)),
                ('a_l_reason', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Accepted_Student_leave',
            fields=[
                ('a_sid', models.AutoField(primary_key=True, serialize=False)),
                ('a_semail', models.CharField(max_length=100)),
                ('a_ss_date', models.DateField(max_length=100)),
                ('a_se_date', models.DateField(max_length=100)),
                ('a_sl_reason', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Module_PM',
            fields=[
                ('Session_key', models.AutoField(primary_key=True, serialize=False)),
                ('Session_value', models.CharField(max_length=100)),
                ('m_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.Chapters')),
            ],
        ),
    ]