# Generated by Django 2.1.5 on 2019-04-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0012_auto_20190414_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='anchor_parent',
        ),
    ]
