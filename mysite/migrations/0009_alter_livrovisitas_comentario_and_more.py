# Generated by Django 4.1.5 on 2023-01-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_produto_artista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livrovisitas',
            name='comentario',
            field=models.TextField(max_length=300, verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='livrovisitas',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='livrovisitas',
            name='recomenda',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=6, verbose_name='Recomendação'),
        ),
    ]
