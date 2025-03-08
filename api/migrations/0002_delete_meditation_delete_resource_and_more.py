# Generated by Django 5.1.6 on 2025-03-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meditation',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='mood',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
