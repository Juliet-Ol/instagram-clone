# Generated by Django 4.0.3 on 2022-04-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
