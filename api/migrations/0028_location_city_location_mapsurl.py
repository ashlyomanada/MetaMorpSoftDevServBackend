# Generated by Django 5.1.7 on 2025-04-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_careerbenefits_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='mapsUrl',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
