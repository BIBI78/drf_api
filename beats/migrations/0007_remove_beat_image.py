# Generated by Django 3.2.23 on 2024-04-21 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0006_alter_beat_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='image',
        ),
    ]
