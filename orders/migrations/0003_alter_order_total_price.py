# Generated by Django 4.1.5 on 2023-01-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_alter_order_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]
