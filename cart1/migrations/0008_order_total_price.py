# Generated by Django 4.1.6 on 2023-05-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart1", "0007_orderitem_total_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
