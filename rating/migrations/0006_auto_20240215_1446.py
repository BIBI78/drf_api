# Generated by Django 3.2.23 on 2024-02-15 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
        ('rating', '0005_auto_20240127_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='post',
        ),
        migrations.AddField(
            model_name='rating',
            name='beat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='beats.beat'),
        ),
    ]
