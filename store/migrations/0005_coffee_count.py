# Generated by Django 5.0.7 on 2024-08-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_coffee_best_seller"),
    ]

    operations = [
        migrations.AddField(
            model_name="coffee",
            name="count",
            field=models.IntegerField(default=5),
        ),
    ]
