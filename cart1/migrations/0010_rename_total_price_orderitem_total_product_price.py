# Generated by Django 4.1.6 on 2023-05-12 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart1", "0009_alter_orderitem_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="total_price",
            new_name="total_product_price",
        ),
    ]
