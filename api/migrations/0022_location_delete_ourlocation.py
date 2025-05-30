# Generated by Django 5.1.7 on 2025-04-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_ourlocation_ourservices_delete_aboutuxui'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('office', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='OurLocation',
        ),
    ]
