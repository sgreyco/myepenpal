# Generated by Django 3.0.6 on 2020-05-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtext', '0002_auto_20200508_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='register_date',
        ),
    ]
