# Generated by Django 5.0.7 on 2024-08-21 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="coffee",
            old_name="discount_per",
            new_name="discount_price",
        ),
    ]
