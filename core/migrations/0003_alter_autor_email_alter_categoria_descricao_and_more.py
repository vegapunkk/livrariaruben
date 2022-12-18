# Generated by Django 4.1.4 on 2022-12-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_livro_capa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="categoria",
            name="descricao",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name="livro",
            name="quantidade",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="cpf",
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]
