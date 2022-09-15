# Generated by Django 4.1.1 on 2022-09-15 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_delete_recurso"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recurso",
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
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "descricao",
                    models.CharField(max_length=100, verbose_name="Descricao"),
                ),
                (
                    "icone",
                    models.CharField(
                        choices=[
                            ("lni-cog", "Engrenagem"),
                            ("lni-stats-up", "Gráfico"),
                            ("lni-user", "Usuário"),
                            ("lni-layers", "Design"),
                            ("lni-mobile", "Mobile"),
                            ("lni-rocket", "Foguete"),
                        ],
                        max_length=12,
                        verbose_name="Icone",
                    ),
                ),
            ],
            options={
                "verbose_name": "Recurso",
                "verbose_name_plural": "Recursos",
            },
        ),
    ]