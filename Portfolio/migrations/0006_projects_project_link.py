# Generated by Django 3.2.8 on 2021-11-10 12:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_remove_projects_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Project_link',
            field=tinymce.models.HTMLField(default='Yes'),
        ),
    ]
