# Generated by Django 3.2.4 on 2021-06-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsite', '0006_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(default='Tag of the blog', max_length=255),
        ),
    ]
