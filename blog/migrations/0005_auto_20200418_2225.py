# Generated by Django 2.2 on 2020-04-19 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='object_id',
        ),
        migrations.AddField(
            model_name='vote',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment'),
        ),
        migrations.AddField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
