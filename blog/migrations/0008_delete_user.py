# Generated by Django 4.1.3 on 2022-12-21 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
