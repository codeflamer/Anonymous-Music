# Generated by Django 2.1.2 on 2019-03-10 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190310_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='User2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
