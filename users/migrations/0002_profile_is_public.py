# Generated by Django 2.2 on 2020-12-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
