# Generated by Django 4.0.1 on 2022-01-08 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="img",
            new_name="image",
        ),
    ]
