# Generated by Django 2.1.5 on 2019-04-16 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0014_response_anchor_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='message',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='response_id',
        ),
    ]
