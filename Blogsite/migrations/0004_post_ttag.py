# Generated by Django 3.2.4 on 2021-06-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsite', '0003_rename_postt_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ttag',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
