# Generated by Django 4.2.8 on 2024-01-08 23:04

import appgestaoimoveis.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appgestaoimoveis", "0006_contratos_valor_aluguel_currency_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contratos",
            name="data_base",
            field=models.DateField(
            ),
        ),
    ]
