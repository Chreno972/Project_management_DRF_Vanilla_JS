# Generated by Django 3.0.3 on 2022-04-09 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('project_type', models.CharField(blank=True, max_length=200, null=True)),
                ('materials_source', models.CharField(blank=True, max_length=200, null=True)),
                ('usability_level', models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')], max_length=50)),
            ],
        ),
    ]
