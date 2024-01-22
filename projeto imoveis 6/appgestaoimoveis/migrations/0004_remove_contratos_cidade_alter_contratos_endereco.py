# Generated by Django 4.2.8 on 2024-01-08 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("appgestaoimoveis", "0003_remove_contratos_inquilino_contratos_nome"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contratos",
            name="cidade",
        ),
        migrations.AlterField(
            model_name="contratos",
            name="endereco",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="appgestaoimoveis.imoveis",
            ),
        ),
    ]
