# Generated by Django 2.2 on 2020-11-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='messages',
            field=models.ManyToManyField(related_name='thread', to='messenger.Message'),
        ),
    ]
