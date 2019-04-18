# Generated by Django 2.1.5 on 2019-04-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_auto_20190414_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='anchor_parent',
        ),
        migrations.AddField(
            model_name='response',
            name='anchor_parent',
            field=models.ManyToManyField(blank=True, null=True, related_name='_response_anchor_parent_+', to='contents.Response'),
        ),
    ]