# Generated by Django 4.2.8 on 2024-01-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contratos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inquilino", models.CharField(max_length=255)),
                ("cidade", models.CharField(max_length=255)),
                ("endereco", models.CharField(max_length=255)),
                ("valor_aluguel", models.DecimalField(decimal_places=2, max_digits=10)),
                ("data_base", models.DateField()),
                ("indice", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Imoveis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cidade", models.CharField(max_length=50)),
                ("endereco", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Inquilinos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("cpfcnpj", models.CharField(max_length=50)),
            ],
        ),
    ]
