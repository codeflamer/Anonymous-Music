# Generated by Django 2.1.2 on 2019-01-29 20:09

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('london', django.db.models.manager.Manager()),
            ],
        ),
    ]
