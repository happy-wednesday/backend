# Generated by Django 2.1.5 on 2019-04-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_thread_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='response_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='response_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
