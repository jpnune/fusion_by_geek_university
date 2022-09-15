# Generated by Django 4.1.1 on 2022-09-14 22:42

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cargo",
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
                ("cargo", models.CharField(max_length=100, verbose_name="Cargo")),
            ],
            options={
                "verbose_name": "Cargo",
                "verbose_name_plural": "Cargos",
            },
        ),
        migrations.CreateModel(
            name="Servico",
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
                ("servico", models.CharField(max_length=100, verbose_name="Serviço")),
                (
                    "descricao",
                    models.TextField(max_length=200, verbose_name="Descrição"),
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
                "verbose_name": "Serviço",
                "verbose_name_plural": "Serviços",
            },
        ),
        migrations.CreateModel(
            name="Funcionario",
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
                ("bio", models.TextField(max_length=200, verbose_name="Bio")),
                (
                    "imagem",
                    stdimage.models.StdImageField(
                        force_min_size=False,
                        upload_to="equipe",
                        variations={
                            "thumb": {"crop": True, "height": 480, "width": 480}
                        },
                        verbose_name="Imagem",
                    ),
                ),
                (
                    "facebook",
                    models.CharField(
                        default="#", max_length=100, verbose_name="Facebook"
                    ),
                ),
                (
                    "twittwer",
                    models.CharField(
                        default="#", max_length=100, verbose_name="Twitter"
                    ),
                ),
                (
                    "instagran",
                    models.CharField(
                        default="#", max_length=100, verbose_name="Instagran"
                    ),
                ),
                (
                    "cargo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.cargo",
                        verbose_name="Cargo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Funcionário",
                "verbose_name_plural": "Funcionários",
            },
        ),
    ]
