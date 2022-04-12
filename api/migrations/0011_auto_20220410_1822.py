# Generated by Django 3.0.3 on 2022-04-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220409_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='sources',
        ),
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='website_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
