# Generated by Django 4.1.6 on 2023-05-08 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_rename_mymodel_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
    ]