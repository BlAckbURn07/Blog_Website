# Generated by Django 3.2.4 on 2021-06-13 13:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogsite', '0002_rename_post_postt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postt',
            new_name='Post',
        ),
    ]
