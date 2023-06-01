# Generated by Django 4.1.6 on 2023-05-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart1", "0012_alter_order_options_remove_orderitem_total_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]