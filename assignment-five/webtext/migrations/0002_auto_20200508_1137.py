# Generated by Django 3.0.6 on 2020-05-08 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtext', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
