# Generated by Django 3.2.23 on 2024-03-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', max_length=300, upload_to='images/'),
        ),
    ]

    