# Generated by Django 4.2.4 on 2023-11-30 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_blogpost_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='thumbnail',
            new_name='image',
        ),
    ]