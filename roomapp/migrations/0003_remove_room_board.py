# Generated by Django 3.2.9 on 2021-11-12 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0002_auto_20211112_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='board',
        ),
    ]
