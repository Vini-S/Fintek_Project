# Generated by Django 2.2.2 on 2019-06-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_auto_20190626_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_view',
            name='c_code',
        ),
        migrations.AlterField(
            model_name='course',
            name='c_code',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
