# Generated by Django 3.2.8 on 2021-11-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='Subtitle',
        ),
        migrations.AddField(
            model_name='projects',
            name='Description',
            field=models.TextField(default='Yes', null=True),
        ),
    ]