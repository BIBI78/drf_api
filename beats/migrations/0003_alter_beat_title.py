# Generated by Django 3.2.23 on 2024-04-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0002_alter_beat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
