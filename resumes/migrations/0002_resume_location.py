# Generated by Django 5.1.4 on 2024-12-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
