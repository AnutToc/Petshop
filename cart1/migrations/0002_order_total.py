# Generated by Django 4.1.6 on 2023-05-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
