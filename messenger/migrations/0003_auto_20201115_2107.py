# Generated by Django 2.2 on 2020-11-15 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20201115_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='messages',
        ),
        migrations.AddField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='messenger.Thread'),
            preserve_default=False,
        ),
    ]
