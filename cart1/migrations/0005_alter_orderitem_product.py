# Generated by Django 4.1.6 on 2023-05-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart1", "0004_rename_total_order_total_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.CharField(max_length=255),
        ),
    ]
