# Generated by Django 4.1.6 on 2023-05-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0011_product_image_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="password",
            field=models.CharField(
                db_column="password", default="default_password", max_length=128
            ),
        ),
    ]