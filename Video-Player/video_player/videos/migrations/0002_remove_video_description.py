# Generated by Django 4.2.7 on 2023-11-17 02:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="description",
        ),
    ]