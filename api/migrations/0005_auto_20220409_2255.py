# Generated by Django 3.0.3 on 2022-04-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='materials',
            field=models.ManyToManyField(to='api.Materials'),
        ),
    ]
