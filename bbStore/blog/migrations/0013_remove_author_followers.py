# Generated by Django 4.2.1 on 2024-01-08 08:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0012_author_followers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="followers",
        ),
    ]
